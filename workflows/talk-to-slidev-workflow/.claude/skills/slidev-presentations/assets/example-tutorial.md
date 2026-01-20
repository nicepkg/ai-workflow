---
theme: default
title: TypeScript Fundamentals
info: |
  ## Getting Started with TypeScript
  A hands-on workshop for JavaScript developers
highlighter: shiki
transition: fade
mdc: true
lineNumbers: true
download: true
exportFilename: typescript-workshop
---

# TypeScript Fundamentals

A Hands-On Workshop for JavaScript Developers

<div class="abs-br m-6 flex gap-2">
  <a href="https://www.typescriptlang.org/" target="_blank" class="text-sm opacity-50 !border-none">
    typescriptlang.org
  </a>
</div>

<!--
Workshop overview:
- 90 minutes total
- Mix of theory and exercises
- Questions welcome throughout
-->

---

## What We'll Cover

<v-clicks>

1. **Why TypeScript?** - The problem it solves
2. **Basic Types** - Primitives, arrays, objects
3. **Functions** - Parameters, return types, overloads
4. **Interfaces vs Types** - When to use each
5. **Generics** - Reusable, type-safe code
6. **Practical Patterns** - Real-world applications

</v-clicks>

<v-click>

<div class="mt-8 p-4 bg-green-500 bg-opacity-10 rounded">
📁 <strong>Workshop repo:</strong> <code>github.com/example/ts-workshop</code>
</div>

</v-click>

---

## layout: two-cols

## JavaScript's Challenge

```javascript
function calculateTotal(items) {
  return items.reduce(
    (sum, item) => sum + item.price,
    0
  )
}

// All of these "work"...
calculateTotal([{ price: 10 }])  // 10
calculateTotal([{ cost: 10 }])   // NaN
calculateTotal("hello")          // Error!
calculateTotal(null)             // Error!
```

::right::

<div class="pl-4">

### The Problem

<v-clicks>

- No compile-time safety
- Errors found at runtime
- IDE can't help you
- Refactoring is scary
- Documentation gets stale

</v-clicks>

</div>

---

## layout: two-cols

## TypeScript's Solution

```typescript
interface CartItem {
  name: string
  price: number
  quantity: number
}

function calculateTotal(
  items: CartItem[]
): number {
  return items.reduce(
    (sum, item) =>
      sum + item.price * item.quantity,
    0
  )
}
```

::right::

<div class="pl-4">

### The Benefits

<v-clicks>

- Errors caught at compile time
- Full IDE autocomplete
- Self-documenting code
- Safe refactoring
- Better team collaboration

</v-clicks>

</div>

---

## Basic Types

```typescript {1-2|4-5|7-8|10-11|13-14|all}
// Primitives
let name: string = "Alice"
let age: number = 30
let active: boolean = true

// Arrays
let scores: number[] = [95, 87, 92]
let names: Array<string> = ["Alice", "Bob"]

// Tuple (fixed-length array)
let pair: [string, number] = ["age", 30]

// Any (escape hatch - avoid!)
let data: any = "could be anything"

// Unknown (safer than any)
let input: unknown = getUserInput()
```

<v-click>

<div class="mt-4 text-yellow-500">
⚠️ Avoid <code>any</code> - it disables type checking entirely
</div>

</v-click>

---

## Objects and Interfaces

```typescript {1-6|8-13|15-20|all}
// Inline object type
let user: { name: string; age: number } = {
  name: "Alice",
  age: 30
}

// Interface (preferred for objects)
interface User {
  id: number
  name: string
  email: string
  age?: number  // Optional property
}

// Using the interface
const alice: User = {
  id: 1,
  name: "Alice",
  email: "alice@example.com"
  // age is optional, so we can omit it
}
```

---

## Exercise 1: Define Types

<div class="text-lg mb-4">
Create types for a blog post system
</div>

```typescript
// TODO: Define these types

// A blog post has:
// - id (number)
// - title (string)
// - content (string)
// - author (string)
// - publishedAt (Date, optional)
// - tags (array of strings)

// An author has:
// - id (number)
// - name (string)
// - bio (string, optional)
// - posts (array of blog posts)
```

<v-click>

<div class="mt-4 p-3 bg-blue-500 bg-opacity-10 rounded">
⏱️ <strong>5 minutes</strong> - Try it in your editor!
</div>

</v-click>

---

## Exercise 1: Solution

```typescript
interface BlogPost {
  id: number
  title: string
  content: string
  author: string
  publishedAt?: Date
  tags: string[]
}

interface Author {
  id: number
  name: string
  bio?: string
  posts: BlogPost[]
}
```

---

## Functions

```typescript {1-4|6-11|13-19|all}
// Basic function typing
function greet(name: string): string {
  return `Hello, ${name}!`
}

// Arrow function
const add = (a: number, b: number): number => {
  return a + b
}

// Optional and default parameters
function createUser(
  name: string,
  age?: number,
  role: string = "user"
): User {
  return { name, age, role }
}

createUser("Alice")           // OK
createUser("Bob", 25)         // OK
createUser("Charlie", 30, "admin")  // OK
```

---

## Generics: Reusable Types

```typescript {1-5|7-13|15-21|all}
// Without generics - loses type info
function firstElement(arr: any[]): any {
  return arr[0]
}

// With generics - preserves types!
function firstElement<T>(arr: T[]): T | undefined {
  return arr[0]
}

const num = firstElement([1, 2, 3])      // type: number
const str = firstElement(["a", "b"])     // type: string

// Generic interface
interface ApiResponse<T> {
  data: T
  status: number
  message: string
}

const userResponse: ApiResponse<User> = {
  data: { id: 1, name: "Alice", email: "a@b.com" },
  status: 200,
  message: "Success"
}
```

---

## layout: two-cols-header

## Type vs Interface

::left::

### Interface

```typescript
interface User {
  name: string
  age: number
}

// Extends another interface
interface Admin extends User {
  permissions: string[]
}

// Declaration merging
interface User {
  email: string  // Added!
}
```

**Use for:** Object shapes, classes

::right::

### Type

```typescript
type User = {
  name: string
  age: number
}

// Intersection
type Admin = User & {
  permissions: string[]
}

// Unions (interface can't do this)
type Status = "loading" | "success" | "error"
type ID = string | number
```

**Use for:** Unions, primitives, tuples

---

## Real-World Pattern: API Client

```typescript {all|1-7|9-15|17-26|all}
// Define your API response types
interface User {
  id: number
  name: string
  email: string
}

// Generic fetch wrapper
async function fetchApi<T>(url: string): Promise<T> {
  const response = await fetch(url)
  if (!response.ok) {
    throw new Error(`HTTP ${response.status}`)
  }
  return response.json()
}

// Usage - fully typed!
async function getUser(id: number): Promise<User> {
  return fetchApi<User>(`/api/users/${id}`)
}

const user = await getUser(123)
console.log(user.name)  // ✅ Autocomplete works!
console.log(user.foo)   // ❌ Error: Property 'foo' does not exist
```

---

layout: center
class: text-center

---

## Key Takeaways

<v-clicks>

**Start gradually** → Add types to new code first

**Use strict mode** → `"strict": true` in tsconfig

**Prefer interfaces** → For object shapes

**Embrace generics** → For reusable utilities

**Avoid `any`** → Use `unknown` if truly unknown

</v-clicks>

---

## layout: end

## Workshop Complete

<div class="mt-8">

**Resources:**

- 📖 [TypeScript Handbook](https://www.typescriptlang.org/docs/handbook/)
- 🎮 [TypeScript Playground](https://www.typescriptlang.org/play)
- 📦 Workshop code: `github.com/example/ts-workshop`

</div>
