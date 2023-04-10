# Backend - FastAPI + poetry
This is where the API and any python or backend system functionality should reside. Use tinyDB to store any chat and system data. An integration with Pinecone DB and Supabase could also be integrated here, along with system and broader network access. 

To run you'll need poetry. Add a `.env` file with `OPENAI_API_KEY={insert your api key here}`. You may need to install a plugin for poetry/python to find your key (e.g. url) just export it with `export=OPENAI_API_KEY`