def find_text_in_file(file_path, search_text):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
    except FileNotFoundError:
        print(f"file {file_path} not found.")
        return
    except Exception as e:
        print(f"Error in search of these files: {e}")
        return
    start = 0
    while True:
        start = content.find(search_text, start)
        if start == -1:
            break
        start_index = max(start - 200, 20)  
        end_index = start + len(search_text) + 20
        snippet = content[start_index:end_index]
        print(f"Was found: \n{snippet}\n{'-'*200}")
        start += len(search_text)
WAITER = 1
DO_NOT_BREAK = True
if __name__ == "__main__":
    file_path = input("Enter name of file in the same Directory with search.py: ")
    search_text = input("Enter the searchable tet: ")
    find_text_in_file(file_path, search_text)

while DO_NOT_BREAK == True:
    WAITER += 1
