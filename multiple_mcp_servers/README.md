# mcp-samples

The client will:
1. Connect to the weather server via stdio
2. Initialize a session
3. Load MCP tools
4. Create a ReAct agent using GPT-4
5. Process weather queries like "What's the weather in New York?"

## Note
There appears to be a typo in the model name in `client.py`. It should be `"gpt-4"` instead of `"gpt-4o"`.

## Run
```bash
make run
```

The weather server will always return "It's always sunny in New York" regardless of the input location.

```
# output

➜  multiple_mcp_servers git:(master) ✗ python weather_server.py
INFO:     Started server process [66790]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     127.0.0.1:51407 - "GET /sse HTTP/1.1" 200 OK
INFO:     127.0.0.1:51409 - "POST /messages/?session_id=9a8b55868ab74889bba07fa43cf64c0f HTTP/1.1" 202 Accepted
INFO:     127.0.0.1:51409 - "POST /messages/?session_id=9a8b55868ab74889bba07fa43cf64c0f HTTP/1.1" 202 Accepted
INFO:     127.0.0.1:51409 - "POST /messages/?session_id=9a8b55868ab74889bba07fa43cf64c0f HTTP/1.1" 202 Accepted
Processing request of type ListToolsRequest
INFO:     127.0.0.1:51419 - "POST /messages/?session_id=9a8b55868ab74889bba07fa43cf64c0f HTTP/1.1" 202 Accepted
Processing request of type CallToolRequest
```

```
➜  multiple_mcp_servers git:(master) ✗ python client.py
Processing request of type ListToolsRequest
Processing request of type CallToolRequest
Processing request of type CallToolRequest

Math Query Result:
{'messages': [HumanMessage(content="what's (3 + 5) x 12?", additional_kwargs={}, response_metadata={}, id='eadfa70c-fbf2-478c-a3bb-fd54ab7df485'), AIMessage(content='', additional_kwargs={'tool_calls': [{'id': 'call_cd8reV7leu15FMqZ1IK0JbQI', 'function': {'arguments': '{"a":3,"b":5}', 'name': 'add'}, 'type': 'function'}], 'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 18, 'prompt_tokens': 96, 'total_tokens': 114, 'completion_tokens_details': {'accepted_prediction_tokens': 0, 'audio_tokens': 0, 'reasoning_tokens': 0, 'rejected_prediction_tokens': 0}, 'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}}, 'model_name': 'gpt-4o-2024-08-06', 'system_fingerprint': 'fp_eb9dce56a8', 'finish_reason': 'tool_calls', 'logprobs': None}, id='run-74e6319c-1844-41c7-b99a-b7197e737151-0', tool_calls=[{'name': 'add', 'args': {'a': 3, 'b': 5}, 'id': 'call_cd8reV7leu15FMqZ1IK0JbQI', 'type': 'tool_call'}], usage_metadata={'input_tokens': 96, 'output_tokens': 18, 'total_tokens': 114, 'input_token_details': {'audio': 0, 'cache_read': 0}, 'output_token_details': {'audio': 0, 'reasoning': 0}}), ToolMessage(content='8', name='add', id='9d21d096-99f9-4b5a-a136-f3bc5b2ff448', tool_call_id='call_cd8reV7leu15FMqZ1IK0JbQI'), AIMessage(content='', additional_kwargs={'tool_calls': [{'id': 'call_xmqHHEZ4sO7W5HD5N3B45Pv1', 'function': {'arguments': '{"a":8,"b":12}', 'name': 'multiply'}, 'type': 'function'}], 'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 18, 'prompt_tokens': 121, 'total_tokens': 139, 'completion_tokens_details': {'accepted_prediction_tokens': 0, 'audio_tokens': 0, 'reasoning_tokens': 0, 'rejected_prediction_tokens': 0}, 'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}}, 'model_name': 'gpt-4o-2024-08-06', 'system_fingerprint': 'fp_eb9dce56a8', 'finish_reason': 'tool_calls', 'logprobs': None}, id='run-5943e111-0d9e-4a1a-99e8-4e6b9130976c-0', tool_calls=[{'name': 'multiply', 'args': {'a': 8, 'b': 12}, 'id': 'call_xmqHHEZ4sO7W5HD5N3B45Pv1', 'type': 'tool_call'}], usage_metadata={'input_tokens': 121, 'output_tokens': 18, 'total_tokens': 139, 'input_token_details': {'audio': 0, 'cache_read': 0}, 'output_token_details': {'audio': 0, 'reasoning': 0}}), ToolMessage(content='96', name='multiply', id='b9306fa1-3d01-4780-8470-39948de55093', tool_call_id='call_xmqHHEZ4sO7W5HD5N3B45Pv1'), AIMessage(content='The result of \\((3 + 5) \\times 12\\) is 96.', additional_kwargs={'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 22, 'prompt_tokens': 146, 'total_tokens': 168, 'completion_tokens_details': {'accepted_prediction_tokens': 0, 'audio_tokens': 0, 'reasoning_tokens': 0, 'rejected_prediction_tokens': 0}, 'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}}, 'model_name': 'gpt-4o-2024-08-06', 'system_fingerprint': 'fp_eb9dce56a8', 'finish_reason': 'stop', 'logprobs': None}, id='run-48db9c8f-4408-4d30-a038-d93fb993a101-0', usage_metadata={'input_tokens': 146, 'output_tokens': 22, 'total_tokens': 168, 'input_token_details': {'audio': 0, 'cache_read': 0}, 'output_token_details': {'audio': 0, 'reasoning': 0}})]}

Weather Query Result:
{'messages': [HumanMessage(content='what is the weather in nyc?', additional_kwargs={}, response_metadata={}, id='9f49caff-cfd8-4a81-8684-6e9f82319e87'), AIMessage(content='', additional_kwargs={'tool_calls': [{'id': 'call_BXmafQLZkIVukBjjs4t97C3R', 'function': {'arguments': '{"location":"nyc"}', 'name': 'get_weather'}, 'type': 'function'}], 'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 16, 'prompt_tokens': 92, 'total_tokens': 108, 'completion_tokens_details': {'accepted_prediction_tokens': 0, 'audio_tokens': 0, 'reasoning_tokens': 0, 'rejected_prediction_tokens': 0}, 'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}}, 'model_name': 'gpt-4o-2024-08-06', 'system_fingerprint': 'fp_eb9dce56a8', 'finish_reason': 'tool_calls', 'logprobs': None}, id='run-1bb1733d-94ff-4518-a476-24ca9730c882-0', tool_calls=[{'name': 'get_weather', 'args': {'location': 'nyc'}, 'id': 'call_BXmafQLZkIVukBjjs4t97C3R', 'type': 'tool_call'}], usage_metadata={'input_tokens': 92, 'output_tokens': 16, 'total_tokens': 108, 'input_token_details': {'audio': 0, 'cache_read': 0}, 'output_token_details': {'audio': 0, 'reasoning': 0}}), ToolMessage(content="It's always sunny in New York", name='get_weather', id='253bd779-b0f7-4644-9494-3dc37cfa4d06', tool_call_id='call_BXmafQLZkIVukBjjs4t97C3R'), AIMessage(content='The weather in New York City is currently sunny.', additional_kwargs={'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 12, 'prompt_tokens': 121, 'total_tokens': 133, 'completion_tokens_details': {'accepted_prediction_tokens': 0, 'audio_tokens': 0, 'reasoning_tokens': 0, 'rejected_prediction_tokens': 0}, 'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}}, 'model_name': 'gpt-4o-2024-08-06', 'system_fingerprint': 'fp_eb9dce56a8', 'finish_reason': 'stop', 'logprobs': None}, id='run-263e853e-d5af-4f0e-878d-ff4e7c28540f-0', usage_metadata={'input_tokens': 121, 'output_tokens': 12, 'total_tokens': 133, 'input_token_details': {'audio': 0, 'cache_read': 0}, 'output_token_details': {'audio': 0, 'reasoning': 0}})]}
```