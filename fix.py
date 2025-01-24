import re

# Path to the generated main.go file
file_path = "etlx.go"

# Read the file
with open(file_path, mode = "r", encoding="utf-8") as file:
    content = file.read()

# Remove lines importing internal packages
content = re.sub(r'^.*"github\.com/realdatadriven/etlx/internal/.*".*\n', '', content, flags=re.MULTILINE)

# Replace `db.` with `etlx.`
content = content.replace("db.", "etlx.")

# Replace `etlxlib.` with `etlx.`
content = content.replace("etlxlib.", "etlx.")

# Write the updated content back to the file
with open(file_path, mode = "w", encoding="utf-8") as file:
    file.write(content)

print("main.go successfully updated.")
