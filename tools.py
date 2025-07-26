#SERPER_API_KEY=""
from crewai_tools import SerperDevTool
import os
from dotenv import load_dotenv

load_dotenv()

# Setup the tool for internet searching capabilities
google_search_tool = SerperDevTool()


