import requests
import os
import uuid
import json
from flask import Flask, render_template
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
