# Chapter 6 — Tool Engineering

Agents become operationally useful when they can interact with files, applications, databases and services. Tool access, however, introduces ambiguity and risk unless interfaces are carefully engineered. This chapter teaches readers to design narrow tools with typed inputs, structured results and explicit failure behaviour. The SDR Lab gains tools for web research, file access and local data processing. Readers also learn that tool quality frequently affects agent performance more than additional prompting.

## 6.1 Models That Reason and Tools That Act

The model interprets the task and decides what information or action is needed. Tools perform deterministic operations such as retrieving a webpage, reading a file, validating a schema or writing an artifact.

Separating these responsibilities improves reliability. The model should not simulate access to information that a real tool can retrieve, and tools should not contain hidden business judgment that belongs in the reasoning layer.

## 6.2 Designing Narrow and Understandable Tools

A tool should perform one coherent operation with a clear outcome. Broad interfaces such as `complete_sales_task()` make it difficult for the model to predict behaviour or recover from failure.

Narrow tools such as `search_company_news()`, `fetch_webpage()` and `save_account_brief()` are easier to test and authorize. Their side effects are also more visible.

## 6.3 Tool Names, Descriptions and Parameters

Language models select tools partly from their names and descriptions. Ambiguous or overlapping descriptions can lead to incorrect tool selection even when the underlying code is sound.

Parameters should be typed, constrained and documented with examples where ambiguity is likely. Required and optional values should match the tool's real operational needs.

## 6.4 Structured Tool Results

Tool results should return concise, predictable objects rather than large blocks of undifferentiated text. They should include status, relevant data, metadata and errors.

Large results may be saved as artifacts while only a summary and reference are returned to the model. This protects the context window and prepares for later context-management techniques.

## 6.5 Tool Errors, Timeouts and Permissions

Tools should distinguish invalid input, unavailable resources, timeouts, authorization failures and empty results. Returning the same generic exception for every problem prevents intelligent recovery.

Each tool also needs an explicit permission level. Research agents may read public information, while write operations and external communications remain unavailable or approval-gated.

## 6.6 Building Web, File and Data Tools

Readers will implement or configure the initial toolset used by the Account Research Skill. The tools will support search, webpage retrieval, local file access, JSON validation and artifact storage.

Each tool will receive a basic test suite containing successful, invalid and failure cases. The agent will then be evaluated on whether it selects the correct tool and interprets its result accurately.
