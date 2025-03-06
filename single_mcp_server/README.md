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

{
	'messages': [HumanMessage(content = "what's (3 + 5) x 12?", additional_kwargs = {}, response_metadata = {}, id = '2cda7bd5-8ad3-4dca-aba0-ea4db3d478e7'), AIMessage(content = '', additional_kwargs = {
		'tool_calls': [{
			'id': 'call_ZOLKVPoN4Fr6bMxEtFRtebfD',
			'function': {
				'arguments': '{\n  "a": 3,\n  "b": 5\n}',
				'name': 'add'
			},
			'type': 'function'
		}],
		'refusal': None
	}, response_metadata = {
		'token_usage': {
			'completion_tokens': 22,
			'prompt_tokens': 81,
			'total_tokens': 103,
			'completion_tokens_details': {
				'accepted_prediction_tokens': 0,
				'audio_tokens': 0,
				'reasoning_tokens': 0,
				'rejected_prediction_tokens': 0
			},
			'prompt_tokens_details': {
				'audio_tokens': 0,
				'cached_tokens': 0
			}
		},
		'model_name': 'gpt-4-0613',
		'system_fingerprint': None,
		'finish_reason': 'tool_calls',
		'logprobs': None
	}, id = 'run-f456789d-f725-4f35-b4b1-3dd58458ddef-0', tool_calls = [{
		'name': 'add',
		'args': {
			'a': 3,
			'b': 5
		},
		'id': 'call_ZOLKVPoN4Fr6bMxEtFRtebfD',
		'type': 'tool_call'
	}], usage_metadata = {
		'input_tokens': 81,
		'output_tokens': 22,
		'total_tokens': 103,
		'input_token_details': {
			'audio': 0,
			'cache_read': 0
		},
		'output_token_details': {
			'audio': 0,
			'reasoning': 0
		}
	}), ToolMessage(content = '8', name = 'add', id = '1effa511-182a-40b1-a36b-b4b9579ced25', tool_call_id = 'call_ZOLKVPoN4Fr6bMxEtFRtebfD'), AIMessage(content = '', additional_kwargs = {
		'tool_calls': [{
			'id': 'call_gj3Z0XPlZtQBDbRMMtr9sKCZ',
			'function': {
				'arguments': '{ "a": 8, "b": 12 }',
				'name': 'multiply'
			},
			'type': 'function'
		}],
		'refusal': None
	}, response_metadata = {
		'token_usage': {
			'completion_tokens': 19,
			'prompt_tokens': 106,
			'total_tokens': 125,
			'completion_tokens_details': {
				'accepted_prediction_tokens': 0,
				'audio_tokens': 0,
				'reasoning_tokens': 0,
				'rejected_prediction_tokens': 0
			},
			'prompt_tokens_details': {
				'audio_tokens': 0,
				'cached_tokens': 0
			}
		},
		'model_name': 'gpt-4-0613',
		'system_fingerprint': None,
		'finish_reason': 'tool_calls',
		'logprobs': None
	}, id = 'run-87456bcb-beda-49b6-b11b-0eb8b51c3669-0', tool_calls = [{
		'name': 'multiply',
		'args': {
			'a': 8,
			'b': 12
		},
		'id': 'call_gj3Z0XPlZtQBDbRMMtr9sKCZ',
		'type': 'tool_call'
	}], usage_metadata = {
		'input_tokens': 106,
		'output_tokens': 19,
		'total_tokens': 125,
		'input_token_details': {
			'audio': 0,
			'cache_read': 0
		},
		'output_token_details': {
			'audio': 0,
			'reasoning': 0
		}
	}), ToolMessage(content = '96', name = 'multiply', id = 'b571713a-0731-451d-be3f-c7934d375a0f', tool_call_id = 'call_gj3Z0XPlZtQBDbRMMtr9sKCZ'), AIMessage(content = 'The result of (3 + 5) x 12 is 96.', additional_kwargs = {
		'refusal': None
	}, response_metadata = {
		'token_usage': {
			'completion_tokens': 18,
			'prompt_tokens': 131,
			'total_tokens': 149,
			'completion_tokens_details': {
				'accepted_prediction_tokens': 0,
				'audio_tokens': 0,
				'reasoning_tokens': 0,
				'rejected_prediction_tokens': 0
			},
			'prompt_tokens_details': {
				'audio_tokens': 0,
				'cached_tokens': 0
			}
		},
		'model_name': 'gpt-4-0613',
		'system_fingerprint': None,
		'finish_reason': 'stop',
		'logprobs': None
	}, id = 'run-97eb699d-12a4-4b04-a2fb-4d885801b4d2-0', usage_metadata = {
		'input_tokens': 131,
		'output_tokens': 18,
		'total_tokens': 149,
		'input_token_details': {
			'audio': 0,
			'cache_read': 0
		},
		'output_token_details': {
			'audio': 0,
			'reasoning': 0
		}
	})]
}