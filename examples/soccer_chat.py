#!/usr/bin/env python3
"""
Soccer memory example using chat_with_memory
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from memvid import MemvidEncoder, chat_with_memory

# Soccer knowledge base
soccer_chunks = [
    "Brazil has won the most World Cups with 5 titles (1958, 1962, 1970, 1994, 2002).",
    "Argentina won the 2022 World Cup in Qatar with Lionel Messi finally achieving his dream.",
    "Pelé is the only player to win 3 World Cups and scored over 1000 career goals.",
    "Diego Maradona is famous for the 'Hand of God' and solo goal vs England in 1986.",
    "Lionel Messi is a 7-time Ballon d'Or winner who finally won the World Cup in 2022.",
    "Cristiano Ronaldo is a 5-time Ballon d'Or winner and all-time Champions League top scorer.",
    "Real Madrid has won the most Champions League titles with 14 trophies.",
    "Barcelona's tiki-taka style revolutionized modern football under Pep Guardiola.",
    "Manchester United has won 13 Premier League titles, the most in the competition.",
    "Arsenal went unbeaten throughout the 2003-04 Premier League season (The Invincibles).",
    "Leicester City achieved a fairytale 5000-1 Premier League title win in 2015-16.",
    "Liverpool's 'Miracle of Istanbul' - came back from 3-0 down vs AC Milan in 2005 Champions League final.",
    "The first World Cup was held in Uruguay in 1930, with Uruguay winning on home soil.",
    "Only 8 nations have won the World Cup: Brazil, Germany, Italy, Argentina, France, Uruguay, Spain, England.",
    "Miroslav Klose (Germany) is the World Cup's all-time top scorer with 16 goals.",
    "Camp Nou (Barcelona) is Europe's largest stadium with 99,354 capacity.",
    "Old Trafford is known as the 'Theatre of Dreams' and home to Manchester United.",
    "El Clásico between Real Madrid and Barcelona is football's biggest rivalry.",
    "The 2026 World Cup will feature 48 teams for the first time.",
    "Neymar's €222 million transfer from Barcelona to PSG in 2017 is still the world record."
]

# Build memory (DB + FAISS index)
# video_path is no longer used.
index_file_path_prefix = "output/soccer_memory_index" # Prefix for .faiss and .indexinfo.json

# Create output directory with subdirectory for sessions
os.makedirs("output/soccer_chat", exist_ok=True) # For chat session exports

# Encode chunks to database and build FAISS index
encoder = MemvidEncoder()
print("Adding soccer chunks to memory...")
encoder.add_chunks(soccer_chunks)
print(f"Building memory files with prefix: {index_file_path_prefix}...")
encoder.build_memory(index_file_path_prefix) # Changed from build_video
print(f"Created soccer memory (DB and index files with prefix: {index_file_path_prefix})")

# API key handling
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    print("\nNote: Set OPENAI_API_KEY environment variable for full LLM responses.")
    print("Without it, you'll only see raw context chunks or LLM-less responses.\n")

# Chat with the memory - interactive session with custom session directory
print("\n⚽ Chat about soccer! Ask questions about the provided facts.")
chat_with_memory(index_file_path_prefix, api_key=api_key, session_dir="output/soccer_chat")