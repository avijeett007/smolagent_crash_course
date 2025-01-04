from smolagents import CodeAgent, HfApiModel

agent = CodeAgent(tools=[], model=HfApiModel(), add_base_tools=True)

agent.run(
    "Why does Mike not know many people in New York?",
    additional_args={"mp3_sound_file_url":'./transformers_recording.mp3'}
)