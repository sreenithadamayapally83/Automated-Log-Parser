import datetime

def pro_parser(file_path):
    # Dictionaries to store categorized data
    stats = {"CRITICAL": 0, "ERROR": 0, "WARNING": 0}
    issue_details = []

    with open(file_path, 'r') as file:
        for line in file:
            # Check for categories
            for level in stats.keys():
                if f"[{level}]" in line:
                    stats[level] += 1
                    issue_details.append(line.strip())

    # Generate a more "Corporate" style report
    report_name = "System_Diagnostic_Report.txt"
    with open(report_name, 'w') as f:
        f.write("MERCEDES-BENZ STYLE DIAGNOSTIC SUMMARY\n") # Just a nod to the goal
        f.write("="*40 + "\n")
        f.write(f"Date: {datetime.datetime.now()}\n")
        f.write(f"Status: {'FAILED' if stats['CRITICAL'] > 0 else 'STABLE'}\n")
        f.write("-" * 40 + "\n")
        for level, count in stats.items():
            f.write(f"{level}: {count}\n")
        f.write("-" * 40 + "\n")
        f.write("LOG DETAILS:\n")
        for issue in issue_details:
            f.write(f"{issue}\n")

    print("Pro Analysis Complete. View 'System_Diagnostic_Report.txt'")

pro_parser("simulation_log.txt")