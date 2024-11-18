# T7-IR-RAG

## Priority Order for Matching:

### Most Important

- CPC classifications (most specific technical field)
- First independent claim (core invention)
- Abstract (technical summary)

### Secondary Importance

- IPC classifications (broader technical field)
- Dependent claims (implementation details)
- Citation relationships

### Supporting Factors

- Description text
- Title similarity
- Family relationships

## Patent Background Information

### Core Identifiers

#### 1. Lens ID

- A unique identifier assigned by The Lens (a patent database)
- Example: "008-016-149-442-710"
- Used as a consistent way to reference a specific patent across different databases

#### 2. Document Number

- The official patent publication number assigned by the patent office
- Example: "10004568"
- Combined with jurisdiction (like 'US') and kind code ('B2') to form complete patent identifier

#### 3. Abstract

- A brief summary (usually 50-150 words) that describes the core invention
- Contains key technical aspects and primary purpose of the patent
- First point of reference for understanding what the patent is about
- Example: "An articulated probe assembly comprises a base, an outer support rod extending through the base..."

### Classification Systems

#### 1. IPCR Codes (International Patent Classification Codes)

- International standardized classification system for organizing patents by technical field
- Hierarchical structure:
  - Section (A) → Class (61) → Subclass (B) → Group (90) → Subgroup (50)

#### 2. CPC Codes (Cooperative Patent Classification)

- More detailed classification system jointly developed by USPTO and EPO
- Similar hierarchical structure to IPC but with more granular categories
- Generally more specific than IPC codes

### Claims Structure

#### 1. Claims

- Legal statements defining the scope of patent protection
- Structured as numbered paragraphs describing what the patent covers

#### 2. Claim Text

- The actual text content of each claim
- Usually an array containing the text of a single claim
- Example: `['1. An articulated probe assembly, comprising: a base...']`

#### 3. All Claims

- A flattened list containing the text of all claims (both independent and dependent)
- Claim 1 is usually the most important (independent) claim defining the core invention
- Dependent claims (2 and up) reference and add limitations to previous claims

### Applications of Classification Systems

Both classification systems help in:

1. Finding similar patents
2. Determining patent examiner assignments
3. Organizing patent databases
4. Patent searching and analysis
