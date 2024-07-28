def create_hierarchical_index(text):
    index = {}
    lines = text.split('\n')
    current_chapter = None
    current_section = None

    for line in lines:
        if "Chapter" in line:
            current_chapter = line
            index[current_chapter] = {}
        elif "Section" in line and current_chapter:
            current_section = line
            index[current_chapter][current_section] = []
        elif current_section:
            index[current_chapter][current_section].append(line)
    
    return index
