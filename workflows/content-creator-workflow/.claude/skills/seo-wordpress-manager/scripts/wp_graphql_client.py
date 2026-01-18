#!/usr/bin/env python3
"""
WordPress GraphQL Client for SEO operations
Handles authentication and API communication
"""

import os
import sys
import json
import base64
import argparse
from pathlib import Path
from typing import Any, Optional
from dataclasses import dataclass

import requests

# Add shared modules to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent / "shared"))
from config_loader import SkillConfig


@dataclass
class WPCredentials:
    """WordPress authentication credentials"""
    graphql_url: str
    username: str
    app_password: str

    def get_auth_header(self) -> dict[str, str]:
        """Generate Basic Auth header"""
        credentials = f"{self.username}:{self.app_password}"
        encoded = base64.b64encode(credentials.encode()).decode()
        return {"Authorization": f"Basic {encoded}"}


class WPGraphQLClient:
    """WordPress GraphQL API client"""

    def __init__(self, credentials: WPCredentials):
        self.credentials = credentials
        self.session = requests.Session()
        self.session.headers.update({
            "Content-Type": "application/json",
            **credentials.get_auth_header()
        })

    def execute(self, query: str, variables: Optional[dict] = None) -> dict[str, Any]:
        """Execute a GraphQL query/mutation"""
        payload = {"query": query}
        if variables:
            payload["variables"] = variables

        response = self.session.post(
            self.credentials.graphql_url,
            json=payload
        )

        if response.status_code != 200:
            raise Exception(f"GraphQL request failed: {response.status_code} - {response.text}")

        result = response.json()

        if "errors" in result:
            errors = result["errors"]
            error_messages = [e.get("message", str(e)) for e in errors]
            raise Exception(f"GraphQL errors: {'; '.join(error_messages)}")

        return result.get("data", {})

    def get_posts_with_seo(
        self,
        limit: int = 100,
        after: Optional[str] = None,
        category: Optional[str] = None
    ) -> dict[str, Any]:
        """Fetch posts with their SEO metadata"""

        if category:
            query = """
            query GetPostsByCategory($first: Int!, $categorySlug: String!) {
                posts(first: $first, where: {categoryName: $categorySlug, status: PUBLISH}) {
                    pageInfo {
                        hasNextPage
                        endCursor
                    }
                    nodes {
                        databaseId
                        title
                        slug
                        uri
                        date
                        modified
                        seo {
                            title
                            metaDesc
                            focuskw
                            canonical
                            opengraphTitle
                            opengraphDescription
                        }
                    }
                }
            }
            """
            variables = {"first": limit, "categorySlug": category}
        else:
            query = """
            query GetPostsWithSEO($first: Int!, $after: String) {
                posts(first: $first, after: $after, where: {status: PUBLISH}) {
                    pageInfo {
                        hasNextPage
                        endCursor
                    }
                    nodes {
                        databaseId
                        title
                        slug
                        uri
                        date
                        modified
                        seo {
                            title
                            metaDesc
                            focuskw
                            canonical
                            opengraphTitle
                            opengraphDescription
                        }
                    }
                }
            }
            """
            variables = {"first": limit, "after": after}

        return self.execute(query, variables)

    def get_all_posts_with_seo(self, category: Optional[str] = None) -> list[dict]:
        """Fetch all posts with pagination"""
        all_posts = []
        after = None
        has_next = True

        while has_next:
            result = self.get_posts_with_seo(limit=100, after=after, category=category)
            posts_data = result.get("posts", {})

            nodes = posts_data.get("nodes", [])
            all_posts.extend(nodes)

            page_info = posts_data.get("pageInfo", {})
            has_next = page_info.get("hasNextPage", False)
            after = page_info.get("endCursor")

            print(f"Fetched {len(all_posts)} posts...", file=sys.stderr)

        return all_posts

    def update_post_seo(
        self,
        post_id: int,
        title: Optional[str] = None,
        meta_desc: Optional[str] = None,
        focus_keyphrase: Optional[str] = None
    ) -> dict[str, Any]:
        """Update SEO fields for a post"""

        mutation = """
        mutation UpdatePostSEO($postId: Int!, $title: String, $metaDesc: String, $focusKeyphrase: String) {
            updatePostSeo(input: {
                postId: $postId
                title: $title
                metaDesc: $metaDesc
                focusKeyphrase: $focusKeyphrase
            }) {
                success
                post {
                    databaseId
                    title
                }
            }
        }
        """

        variables = {"postId": post_id}
        if title is not None:
            variables["title"] = title
        if meta_desc is not None:
            variables["metaDesc"] = meta_desc
        if focus_keyphrase is not None:
            variables["focusKeyphrase"] = focus_keyphrase

        return self.execute(mutation, variables)


def load_credentials_from_config(config_path: Optional[Path] = None) -> WPCredentials:
    """Load WordPress credentials from config or environment"""
    config = SkillConfig("seo-wordpress-manager", config_path)

    return WPCredentials(
        graphql_url=config.require("wordpress.graphql_url") or config.require("WP_GRAPHQL_URL"),
        username=config.require("wordpress.username") or config.require("WP_USERNAME"),
        app_password=config.require("wordpress.app_password") or config.require("WP_APP_PASSWORD")
    )


def main():
    parser = argparse.ArgumentParser(description="WordPress GraphQL Client for SEO")
    parser.add_argument("--action", choices=["list", "get", "test"], default="list",
                        help="Action to perform")
    parser.add_argument("--limit", type=int, default=10, help="Number of posts to fetch")
    parser.add_argument("--category", type=str, help="Filter by category slug")
    parser.add_argument("--all", action="store_true", help="Fetch all posts (paginated)")
    parser.add_argument("--output", type=str, help="Output file path")
    parser.add_argument("--config", type=str, help="Path to config.json")

    args = parser.parse_args()

    # Load config
    config_path = Path(args.config) if args.config else None
    if not config_path:
        # Try default location
        default_config = Path(__file__).parent.parent / "config.json"
        if default_config.exists():
            config_path = default_config

    try:
        credentials = load_credentials_from_config(config_path)
    except ValueError as e:
        print(f"Configuration error: {e}", file=sys.stderr)
        print("Please set WP_GRAPHQL_URL, WP_USERNAME, WP_APP_PASSWORD environment variables", file=sys.stderr)
        print("Or create a config.json file (see config.example.json)", file=sys.stderr)
        sys.exit(1)

    client = WPGraphQLClient(credentials)

    if args.action == "test":
        # Test connection
        try:
            result = client.get_posts_with_seo(limit=1)
            print("Connection successful!")
            print(f"Sample post: {json.dumps(result, indent=2)}")
        except Exception as e:
            print(f"Connection failed: {e}", file=sys.stderr)
            sys.exit(1)

    elif args.action == "list":
        if args.all:
            posts = client.get_all_posts_with_seo(category=args.category)
        else:
            result = client.get_posts_with_seo(limit=args.limit, category=args.category)
            posts = result.get("posts", {}).get("nodes", [])

        output_data = {"posts": posts, "count": len(posts)}

        if args.output:
            with open(args.output, "w", encoding="utf-8") as f:
                json.dump(output_data, f, indent=2, ensure_ascii=False)
            print(f"Saved {len(posts)} posts to {args.output}")
        else:
            print(json.dumps(output_data, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
