py_files=$(git ls-files | grep '\.py')

if [ -z "$py_files" ]; then
  echo "No .js files found in the Git repository."
else
  total_lines=$(echo "$py_files" | xargs wc -l | tail -n1 | awk '{print $1}')
  echo "Total lines of code in .py files: $total_lines"
fi