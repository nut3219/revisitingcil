DIR="./exps/generated"

# Loop through each JSON file in the specified directory
for json_file in $(find $DIR -type f -name "*.json"); do
    # Run the python command with the current JSON file as an argument
    python main.py --config $json_file
done