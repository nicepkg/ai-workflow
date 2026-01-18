# SEO WordPress Manager - Reference Guide

## Yoast SEO Fields

### Primary Fields (Most Common)
| Field | Meta Key | Max Length | Description |
|-------|----------|------------|-------------|
| SEO Title | `_yoast_wpseo_title` | 60 chars | Title shown in search results |
| Meta Description | `_yoast_wpseo_metadesc` | 160 chars | Description in search results |
| Focus Keyphrase | `_yoast_wpseo_focuskw` | N/A | Primary keyword to optimize for |

### Secondary Fields
| Field | Meta Key | Description |
|-------|----------|-------------|
| Canonical URL | `_yoast_wpseo_canonical` | Preferred URL for this content |
| No Index | `_yoast_wpseo_meta-robots-noindex` | Prevent indexing (1 = noindex) |
| No Follow | `_yoast_wpseo_meta-robots-nofollow` | Prevent link following |

### Open Graph Fields
| Field | Meta Key | Description |
|-------|----------|-------------|
| OG Title | `_yoast_wpseo_opengraph-title` | Facebook/social title |
| OG Description | `_yoast_wpseo_opengraph-description` | Facebook/social description |
| OG Image | `_yoast_wpseo_opengraph-image` | Social sharing image URL |

### Twitter Fields
| Field | Meta Key | Description |
|-------|----------|-------------|
| Twitter Title | `_yoast_wpseo_twitter-title` | Twitter card title |
| Twitter Description | `_yoast_wpseo_twitter-description` | Twitter card description |
| Twitter Image | `_yoast_wpseo_twitter-image` | Twitter card image URL |

## GraphQL Queries

### Fetch Posts with SEO Data
```graphql
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
      seo {
        title
        metaDesc
        focuskw
        canonical
        opengraphTitle
        opengraphDescription
        opengraphImage {
          sourceUrl
        }
      }
    }
  }
}
```

### Fetch Posts by Category
```graphql
query GetPostsByCategory($categorySlug: String!, $first: Int!) {
  posts(first: $first, where: {categoryName: $categorySlug, status: PUBLISH}) {
    nodes {
      databaseId
      title
      seo {
        title
        metaDesc
        focuskw
      }
    }
  }
}
```

### Update SEO Mutation
```graphql
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
```

## SEO Best Practices

### Title Optimization
- **Length**: 50-60 characters (Google truncates at ~60)
- **Structure**: `Primary Keyword - Secondary Keyword | Brand`
- **Front-load**: Put important keywords at the beginning
- **Unique**: Each page should have a unique title

### Meta Description Optimization
- **Length**: 150-160 characters (Google truncates at ~160)
- **Include CTA**: Use action words like "Learn", "Discover", "Get"
- **Include keyword**: Natural placement of focus keyphrase
- **Unique**: Each page needs a unique description
- **Compelling**: Think of it as ad copy

### Focus Keyphrase Guidelines
- **One primary keyword** per post
- **Long-tail** keywords often perform better
- **Search intent** alignment is crucial
- **Natural density**: Don't keyword stuff

## Common Issues & Solutions

### Issue: Titles Too Long
**Solution**: Use the `truncate_title()` function to intelligently shorten titles while preserving meaning.

### Issue: Duplicate Meta Descriptions
**Solution**: Run the analyzer to identify duplicates, then generate unique descriptions based on post content.

### Issue: Missing Focus Keyphrases
**Solution**: Analyze post content and titles to suggest relevant keyphrases.

### Issue: Generic Descriptions
**Solution**: Replace default/template descriptions with content-specific ones.

## WordPress Application Password Setup

1. Go to **Users > Profile** in WordPress admin
2. Scroll to **Application Passwords** section
3. Enter a name (e.g., "Claude SEO Manager")
4. Click **Add New Application Password**
5. Copy the generated password (shown once!)
6. Use format: `username:password` for basic auth

## Rate Limiting Recommendations

| Site Size | Batch Size | Delay (seconds) |
|-----------|------------|-----------------|
| Small (<100 posts) | 20 | 0.5 |
| Medium (100-1000) | 10 | 1 |
| Large (1000+) | 5 | 2 |

## Error Handling

| Error Code | Meaning | Solution |
|------------|---------|----------|
| 401 | Unauthorized | Check Application Password |
| 403 | Forbidden | Check user permissions |
| 429 | Rate Limited | Increase delay between requests |
| 500 | Server Error | Check WPGraphQL logs |
