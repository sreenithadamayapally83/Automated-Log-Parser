# Automated-Log-Parser

A Python-based automation utility designed to streamline hardware verification and manufacturing log analysis. This tool replaces manual log-checking by automatically parsing, categorizing, and reporting system health from raw data files.

##  Project Overview
In large-scale engineering environments (like automotive manufacturing or RTL simulation), systems generate thousands of lines of logs. This tool was developed to:
- **Automate Data Extraction:** Quickly identify "needles in the haystack."
- **Prioritize Issues:** Categorize events into **CRITICAL**, **ERROR**, and **WARNING** levels.
- **Generate Insights:** Produce a clean, executive-style diagnostic report with a "Pass/Fail" status based on system logic.

##  Features
- **Categorization Engine:** Uses keyword logic to sort system messages.
- **Automated Reporting:** Outputs a time-stamped text report (`System_Diagnostic_Report.txt`).
- **Scalability:** The logic can be easily adapted for PLC logs, sensor data monitoring, or simulation transcripts.
