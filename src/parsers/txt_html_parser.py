
import os
from src.processing.bold_calculator import bold_calculator_c

BOLD_TAGS = {
    'start': '<b>',
    'end': '</b>'
}

def chunk_size(file_size: int) -> int:
    """
    Determines appropriate chunk size based on file size
    
    Args:
        file_size: Size of file in bytes
    
    Returns:
        Chunk size in bytes
    """
    if file_size < 1000:  # Less than 1KB
        return 100  # 100 byte chunks
    elif file_size < 1024 * 1024:  # Less than 1MB
        return 1024  # 1KB chunks
    elif file_size < 10 * 1024 * 1024:  # Less than 10MB
        return 512 * 1024  # 512KB chunks
    else:
        return 4 * 1024 * 1024  # 4MB chunks for larger files

def bionic_reader_formatter(chunk: str):
    words =  chunk.split(" ")
    printf("WORDDS {words}")
    for word in words:
        num_bold = bold_calculator_c(word)
        word
        print(f"WORDD {num_bold}") 
    return chunk


def chunk_txt_file(file_path: str):
    # 1. Get file size
    file_stats = os.stat(file_path)
    file_size = file_stats.st_size
    target_chunk_size = chunk_size(file_size)
    print(f"File size: {file_size} bytes")  # Let's add more logging
    print(f"Target chunk size: {target_chunk_size} bytes")
    
    current_size = 0  
    current_chunk = []

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        paragraphs = content.split('\n\n')

        for paragraph in paragraphs:
            return bionic_reader_formatter(paragraph)



        print(f"PARAAA {paragraphs}")  # More logging
        print(f"Found {len(paragraphs)} paragraphs")  # More logging
        
        for paragraph in paragraphs:
            paragraph = paragraph.strip()
            
            if not paragraph:
                continue

            para_size = len(paragraph.encode('utf-8')) # Bytes of each chunk
            print(f"Processing paragraph of size {para_size} bytes: {paragraph[:50]}...")  # More logging

            if current_size + para_size > target_chunk_size and current_chunk:
                chunk_text = '\n\n'.join(current_chunk)
                print(f"Yielding chunk of size {current_size} bytes")  # More logging
                yield chunk_text
                current_chunk = []
                current_size = 0

            current_chunk.append(paragraph)
            current_size += para_size
            
    if current_chunk:
        chunk_text = '\n\n'.join(current_chunk)
        print(f"Yielding final chunk of size {current_size} bytes")  # More logging
        yield chunk_text

# Test the function
print("Starting to process file...")  # More logging
for i, chunk in enumerate(chunk_txt_file('src/parsers/demofile.txt')):
    print(f"\nChunk {i+1}:")
    print("-" * 50)
    print(chunk)
    print("-" * 50)