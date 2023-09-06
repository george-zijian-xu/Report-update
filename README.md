# Citic Bank Financial Systems - AI Report Generator
## Project Overview
This project aims to automate the process of generating comprehensive credit reports for publicly traded companies for Citic Bank's Financial Systems department. By leveraging GPT-based AI, the system efficiently searches, organizes, and compiles public information into a user-friendly Word format report.

## Components
### 1. fetchNews
This component is responsible for fetching annual reports of publicly traded companies. These reports serve as the primary data source for generating credit reports.

Features:
Uses various APIs to fetch relevant news.
Focuses on publicly traded companies, ensuring data accuracy and relevance.

### 2. IndexNews
This component processes the fetched news and embeds it into a JSON format, making it more accessible for further processing.
Features:
Converts lengthy reports into structured JSON format.
Makes data more digestible for the GPT-based AI.

### 3. queryMulti
A multi-query system that interacts with ChatGPT to ask multiple questions. The responses are then used to compile the final report.
Features:
Efficiently frames questions to extract relevant information.
Processes and organizes AI-generated responses for report compilation.

### 4. reportFormatting
This component takes the processed data and formats it into a comprehensive Word document, ready for presentation.
