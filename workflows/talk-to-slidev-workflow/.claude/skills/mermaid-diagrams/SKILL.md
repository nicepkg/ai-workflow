---
name: mermaid-diagrams
description: Create diagrams and visualizations using Mermaid syntax. Use when generating flowcharts, sequence diagrams, class diagrams, entity-relationship diagrams, Gantt charts, or any visual documentation. Triggers on Mermaid, flowchart, sequence diagram, class diagram, ER diagram, Gantt chart, diagram, visualization.
---

# Mermaid Diagrams

Create diagrams and visualizations using Mermaid markdown syntax.

## Quick Reference

Mermaid diagrams are written in markdown code blocks with `mermaid` as the language identifier.

## Flowchart

```mermaid
flowchart TD
    A[Start] --> B{Is it valid?}
    B -->|Yes| C[Process data]
    B -->|No| D[Show error]
    C --> E[Save to database]
    D --> F[Return to input]
    E --> G[End]
    F --> A
```

### Flowchart Syntax
```
flowchart TD          %% TD = top-down, LR = left-right, RL, BT
    A[Rectangle]      %% Square brackets = rectangle
    B(Rounded)        %% Parentheses = rounded rectangle
    C{Diamond}        %% Curly braces = diamond/decision
    D[[Subroutine]]   %% Double brackets = subroutine
    E[(Database)]     %% Cylinder shape
    F((Circle))       %% Double parentheses = circle
    G>Asymmetric]     %% Flag shape

    A --> B           %% Arrow
    B --- C           %% Line without arrow
    C -.-> D          %% Dotted arrow
    D ==> E           %% Thick arrow
    E --text--> F     %% Arrow with label
    F -->|label| G    %% Alternative label syntax
```

### Subgraphs
```mermaid
flowchart TB
    subgraph Frontend
        A[React App] --> B[Components]
        B --> C[Hooks]
    end
    
    subgraph Backend
        D[API Server] --> E[Database]
    end
    
    A -->|HTTP| D
```

## Sequence Diagram

```mermaid
sequenceDiagram
    participant U as User
    participant C as Client
    participant S as Server
    participant D as Database

    U->>C: Click submit
    C->>S: POST /api/data
    activate S
    S->>D: INSERT query
    D-->>S: Success
    S-->>C: 200 OK
    deactivate S
    C-->>U: Show success message
```

### Sequence Diagram Syntax
```
sequenceDiagram
    participant A as Alice
    participant B as Bob

    A->>B: Solid line with arrow
    A-->>B: Dotted line with arrow
    A-)B: Solid line with open arrow
    A--)B: Dotted line with open arrow
    
    activate B          %% Activation box
    B->>A: Response
    deactivate B
    
    Note over A,B: This is a note
    Note right of A: Note on right
    
    alt Condition true
        A->>B: Do this
    else Condition false
        A->>B: Do that
    end
    
    loop Every minute
        A->>B: Ping
    end
    
    opt Optional action
        A->>B: Maybe do this
    end
```

## Class Diagram

```mermaid
classDiagram
    class User {
        +String id
        +String name
        +String email
        +login()
        +logout()
    }
    
    class Order {
        +String id
        +Date createdAt
        +calculateTotal()
    }
    
    class Product {
        +String id
        +String name
        +Number price
    }
    
    User "1" --> "*" Order : places
    Order "*" --> "*" Product : contains
```

### Class Diagram Syntax
```
classDiagram
    class ClassName {
        +publicField
        -privateField
        #protectedField
        ~packageField
        +publicMethod()
        -privateMethod()
    }
    
    ClassA <|-- ClassB : Inheritance
    ClassC *-- ClassD : Composition
    ClassE o-- ClassF : Aggregation
    ClassG --> ClassH : Association
    ClassI ..> ClassJ : Dependency
    ClassK ..|> ClassL : Realization
```

## Entity Relationship Diagram

```mermaid
erDiagram
    USER ||--o{ ORDER : places
    ORDER ||--|{ LINE_ITEM : contains
    PRODUCT ||--o{ LINE_ITEM : "is in"
    
    USER {
        string id PK
        string email UK
        string name
        datetime created_at
    }
    
    ORDER {
        string id PK
        string user_id FK
        datetime created_at
        string status
    }
    
    PRODUCT {
        string id PK
        string name
        decimal price
    }
    
    LINE_ITEM {
        string id PK
        string order_id FK
        string product_id FK
        int quantity
    }
```

### ER Diagram Cardinality
```
||--||   One to one
||--o{   One to zero or more
||--|{   One to one or more
}o--o{   Zero or more to zero or more
```

## Gantt Chart

```mermaid
gantt
    title Project Timeline
    dateFormat YYYY-MM-DD
    
    section Planning
    Requirements    :a1, 2024-01-01, 7d
    Design          :a2, after a1, 14d
    
    section Development
    Backend API     :b1, after a2, 21d
    Frontend        :b2, after a2, 28d
    Integration     :b3, after b1, 7d
    
    section Testing
    QA Testing      :c1, after b3, 14d
    Bug Fixes       :c2, after c1, 7d
    
    section Launch
    Deployment      :milestone, after c2, 0d
```

## State Diagram

```mermaid
stateDiagram-v2
    [*] --> Idle
    Idle --> Processing: Submit
    Processing --> Success: Valid
    Processing --> Error: Invalid
    Success --> Idle: Reset
    Error --> Idle: Retry
    Success --> [*]
```

## Pie Chart

```mermaid
pie title Browser Market Share
    "Chrome" : 65
    "Safari" : 19
    "Firefox" : 10
    "Edge" : 4
    "Other" : 2
```

## Git Graph

```mermaid
gitGraph
    commit
    commit
    branch feature
    checkout feature
    commit
    commit
    checkout main
    merge feature
    commit
    branch hotfix
    checkout hotfix
    commit
    checkout main
    merge hotfix
```

## User Journey

```mermaid
journey
    title User Checkout Experience
    section Browse
        View products: 5: User
        Add to cart: 4: User
    section Checkout
        Enter shipping: 3: User
        Enter payment: 2: User
        Confirm order: 5: User
    section Post-Purchase
        Receive confirmation: 5: User, System
        Track shipment: 4: User
```

## Mindmap

```mermaid
mindmap
    root((Project))
        Frontend
            React
            TypeScript
            Tailwind
        Backend
            Node.js
            PostgreSQL
            Redis
        DevOps
            Docker
            Kubernetes
            CI/CD
```

## Styling

```mermaid
flowchart LR
    A[Start]:::green --> B[Process]:::blue --> C[End]:::red
    
    classDef green fill:#22c55e,color:#fff
    classDef blue fill:#3b82f6,color:#fff
    classDef red fill:#ef4444,color:#fff
```

## React Component

```tsx
import mermaid from 'mermaid';
import { useEffect, useRef } from 'react';

mermaid.initialize({
  startOnLoad: true,
  theme: 'neutral', // default, dark, forest, neutral
  securityLevel: 'loose',
});

interface MermaidProps {
  chart: string;
  id?: string;
}

export function Mermaid({ chart, id = 'mermaid-diagram' }: MermaidProps) {
  const ref = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (ref.current) {
      mermaid.render(id, chart).then(({ svg }) => {
        if (ref.current) {
          ref.current.innerHTML = svg;
        }
      });
    }
  }, [chart, id]);

  return <div ref={ref} className="mermaid-container" />;
}

// Usage
<Mermaid
  chart={`
    flowchart LR
      A --> B --> C
  `}
/>
```

## Tips

1. **Direction**: Use `TD` (top-down), `LR` (left-right), `BT` (bottom-top), `RL` (right-left)
2. **Comments**: Use `%%` for comments
3. **Quotes**: Use quotes for labels with special characters: `A["Label with (parentheses)"]`
4. **Line breaks**: Use `<br/>` for multi-line labels

## Resources

- **Mermaid Docs**: https://mermaid.js.org/
- **Live Editor**: https://mermaid.live
- **GitHub Support**: Mermaid works natively in GitHub markdown
