# function_definitions_objects_llm = {
#     "vs_code_version": {
#         "name": "vs_code_version",
#         "description": "description",
#         "parameters": {"type": "object", "properties": {}, "required": [""]},
#     },
#     "make_http_requests_with_uv": {
#         "name": "make_http_requests_with_uv",
#         "description": "extract the http url and query parameters from the given text for example 'uv run --with httpie -- https [URL] installs the Python package httpie and sends a HTTPS request to the URL. Send a HTTPS request to https://httpbin.org/get with the URL encoded parameter country set to India and city set to Chennai. What is the JSON output of the command? (Paste only the JSON body, not the headers)' in this example country: India and city: Chennai are the query parameters",
#         "parameters": {
#             "type": "object",
#             "properties": {
#                 "query_params": {
#                     "type": "object",
#                     "description": "The query parameters to send with the request URL encoded parameters",
#                 },
#             },
#             "required": ["query_params", "url"],
#         },
#     },
#     "run_command_with_npx": {
#         "name": "run_command_with_npx",
#         "description": "description",
#         "parameters": {
#             "type": "object",
#             "properties": {
#                 "text": {
#                     "type": "string",
#                     "description": "The text to extract the data from",
#                 }
#             },
#             "required": ["text"],
#         },
#     },
#     "use_google_sheets": {
#         "name": "use_google_sheets",
#         "description": "description",
#         "parameters": {
#             "type": "object",
#             "properties": {
#                 "text": {
#                     "type": "string",
#                     "description": "The text to extract the data from",
#                 }
#             },
#             "required": ["text"],
#         },
#     },
#     "use_excel": {
#         "name": "use_excel",
#         "description": "description",
#         "parameters": {
#             "type": "object",
#             "properties": {
#                 "text": {
#                     "type": "string",
#                     "description": "The text to extract the data from",
#                 }
#             },
#             "required": ["text"],
#         },
#     },
#     "use_devtools": {
#         "name": "use_devtools",
#         "description": "description",
#         "parameters": {
#             "type": "object",
#             "properties": {
#                 "text": {
#                     "type": "string",
#                     "description": "The text to extract the data from",
#                 }
#             },
#             "required": ["text"],
#         },
#     },
#     "count_wednesdays": {
#         "name": "count_wednesdays",
#         "description": "description",
#         "parameters": {
#             "type": "object",
#             "properties": {
#                 "text": {
#                     "type": "string",
#                     "description": "The text to extract the data from",
#                 }
#             },
#             "required": ["text"],
#         },
#     },
#     "extract_csv_from_a_zip": {
#         "name": "extract_csv_from_a_zip",
#         "description": "description",
#         "parameters": {
#             "type": "object",
#             "properties": {
#                 "text": {
#                     "type": "string",
#                     "description": "The text to extract the data from",
#                 }
#             },
#             "required": ["text"],
#         },
#     },
#     "use_json": {
#         "name": "use_json",
#         "description": "Sorts a JSON array of objects based on specified fields. The function takes a JSON string and an optional list of fields to sort by, with the default being ['age', 'name'].",
#         "parameters": {
#             "type": "object",
#             "properties": {
#                 "jsonStr": {
#                     "type": "string",
#                     "description": "The JSON array of objects to be sorted",
#                 },
#                 "fields": {
#                     "type": "array",
#                     "items": {"type": "string"},
#                     "description": "List of fields to sort by, in order of priority. Default is ['age', 'name'].",
#                     "default": ["age", "name"],
#                 },
#             },
#             "required": ["jsonStr"],
#         },
#     },
#     "multi_cursor_edits_to_convert_to_json": {
#         "name": "multi_cursor_edits_to_convert_to_json",
#         "description": "description",
#         "parameters": {"type": "object", "properties": {}, "required": []},
#     },
#     "css_selectors": {
#         "name": "css_selectors",
#         "description": "Finds HTML elements using CSS selectors and calculates the sum of a specified attribute's values from those elements",
#         "parameters": {
#             "type": "object",
#             "properties": {
#                 "attribute": {
#                     "type": "string",
#                     "description": "The attribute name whose values should be summed (e.g., 'data-value')",
#                 },
#                 "cssSelector": {
#                     "type": "string",
#                     "description": "The CSS selector to find specific elements (e.g., 'div.foo' for all div elements with class 'foo')",
#                 },
#             },
#             "required": ["attribute", "cssSelector"],
#         },
#     },
#     "process_files_with_different_encodings": {
#         "name": "process_files_with_different_encodings",
#         "description": "description",
#         "parameters": {
#             "type": "object",
#             "properties": {
#                 "text": {
#                     "type": "string",
#                     "description": "The text to extract the data from",
#                 }
#             },
#             "required": ["text"],
#         },
#     },
#     "use_github": {
#         "name": "use_github",
#         "description": "description",
#         "parameters": {
#             "type": "object",
#             "properties": {
#                 "text": {
#                     "type": "string",
#                     "description": "The text to extract the data from",
#                 }
#             },
#             "required": ["text"],
#         },
#     },
#     "replace_across_files": {
#         "name": "replace_across_files",
#         "description": "description",
#         "parameters": {
#             "type": "object",
#             "properties": {
#                 "text": {
#                     "type": "string",
#                     "description": "The text to extract the data from",
#                 }
#             },
#             "required": ["text"],
#         },
#     },
#     "list_files_and_attributes": {
#         "name": "list_files_and_attributes",
#         "description": "description",
#         "parameters": {
#             "type": "object",
#             "properties": {
#                 "text": {
#                     "type": "string",
#                     "description": "The text to extract the data from",
#                 }
#             },
#             "required": ["text"],
#         },
#     },
#     "move_and_rename_files": {
#         "name": "move_and_rename_files",
#         "description": "description",
#         "parameters": {
#             "type": "object",
#             "properties": {
#                 "text": {
#                     "type": "string",
#                     "description": "The text to extract the data from",
#                 }
#             },
#             "required": ["text"],
#         },
#     },
#     "compare_files": {
#         "name": "compare_files",
#         "description": "description",
#         "parameters": {
#             "type": "object",
#             "properties": {
#                 "text": {
#                     "type": "string",
#                     "description": "The text to extract the data from",
#                 }
#             },
#             "required": ["text"],
#         },
#     },
#     "sql_ticket_sales": {
#         "name": "sql_ticket_sales",
#         "description": "description",
#         "parameters": {
#             "type": "object",
#             "properties": {
#                 "text": {
#                     "type": "string",
#                     "description": "The text to extract the data from",
#                 }
#             },
#             "required": ["text"],
#         },
#     },
#     "write_documentation_in_markdown": {
#         "name": "write_documentation_in_markdown",
#         "description": "description",
#         "parameters": {
#             "type": "object",
#             "properties": {
#                 "text": {
#                     "type": "string",
#                     "description": "The text to extract the data from",
#                 }
#             },
#             "required": ["text"],
#         },
#     },
#     "compress_an_image": {
#         "name": "compress_an_image",
#         "description": "description",
#         "parameters": {
#             "type": "object",
#             "properties": {
#                 "text": {
#                     "type": "string",
#                     "description": "The text to extract the data from",
#                 }
#             },
#             "required": ["text"],
#         },
#     },
#     "host_your_portfolio_on_github_pages": {
#         "name": "host_your_portfolio_on_github_pages",
#         "description": "description",
#         "parameters": {
#             "type": "object",
#             "properties": {
#                 "text": {
#                     "type": "string",
#                     "description": "The text to extract the data from",
#                 }
#             },
#             "required": ["text"],
#         },
#     },
#     "use_google_colab": {
#         "name": "use_google_colab",
#         "description": "description",
#         "parameters": {
#             "type": "object",
#             "properties": {
#                 "text": {
#                     "type": "string",
#                     "description": "The text to extract the data from",
#                 }
#             },
#             "required": ["text"],
#         },
#     },
#     "use_an_image_library_in_google_colab": {
#         "name": "use_an_image_library_in_google_colab",
#         "description": "description",
#         "parameters": {
#             "type": "object",
#             "properties": {
#                 "text": {
#                     "type": "string",
#                     "description": "The text to extract the data from",
#                 }
#             },
#             "required": ["text"],
#         },
#     },
#     "deploy_a_python_api_to_vercel": {
#         "name": "deploy_a_python_api_to_vercel",
#         "description": "description",
#         "parameters": {
#             "type": "object",
#             "properties": {
#                 "text": {
#                     "type": "string",
#                     "description": "The text to extract the data from",
#                 }
#             },
#             "required": ["text"],
#         },
#     },
#     "create_a_github_action": {
#         "name": "create_a_github_action",
#         "description": "description",
#         "parameters": {
#             "type": "object",
#             "properties": {
#                 "text": {
#                     "type": "string",
#                     "description": "The text to extract the data from",
#                 }
#             },
#             "required": ["text"],
#         },
#     },
#     "push_an_image_to_docker_hub": {
#         "name": "push_an_image_to_docker_hub",
#         "description": "description",
#         "parameters": {
#             "type": "object",
#             "properties": {
#                 "text": {
#                     "type": "string",
#                     "description": "The text to extract the data from",
#                 }
#             },
#             "required": ["text"],
#         },
#     },
#     "write_a_fastapi_server_to_serve_data": {
#         "name": "write_a_fastapi_server_to_serve_data",
#         "description": "description",
#         "parameters": {
#             "type": "object",
#             "properties": {
#                 "text": {
#                     "type": "string",
#                     "description": "The text to extract the data from",
#                 }
#             },
#             "required": ["text"],
#         },
#     },
#     "run_a_local_llm_with_llamafile": {
#         "name": "run_a_local_llm_with_llamafile",
#         "description": "description",
#         "parameters": {
#             "type": "object",
#             "properties": {
#                 "text": {
#                     "type": "string",
#                     "description": "The text to extract the data from",
#                 }
#             },
#             "required": ["text"],
#         },
#     },
#     "llm_sentiment_analysis": {
#         "name": "llm_sentiment_analysis",
#         "description": "description",
#         "parameters": {
#             "type": "object",
#             "properties": {
#                 "text": {
#                     "type": "string",
#                     "description": "The text to extract the data from",
#                 }
#             },
#             "required": ["text"],
#         },
#     },
#     "llm_token_cost": {
#         "name": "llm_token_cost",
#         "description": "description",
#         "parameters": {
#             "type": "object",
#             "properties": {
#                 "text": {
#                     "type": "string",
#                     "description": "The text to extract the data from",
#                 }
#             },
#             "required": ["text"],
#         },
#     },
#     "generate_addresses_with_llms": {
#         "name": "generate_addresses_with_llms",
#         "description": "description",
#         "parameters": {
#             "type": "object",
#             "properties": {
#                 "text": {
#                     "type": "string",
#                     "description": "The text to extract the data from",
#                 }
#             },
#             "required": ["text"],
#         },
#     },
#     "llm_vision": {
#         "name": "llm_vision",
#         "description": "description",
#         "parameters": {
#             "type": "object",
#             "properties": {
#                 "text": {
#                     "type": "string",
#                     "description": "The text to extract the data from",
#                 }
#             },
#             "required": ["text"],
#         },
#     },
#     "llm_embeddings": {
#         "name": "llm_embeddings",
#         "description": "description",
#         "parameters": {
#             "type": "object",
#             "properties": {
#                 "text": {
#                     "type": "string",
#                     "description": "The text to extract the data from",
#                 }
#             },
#             "required": ["text"],
#         },
#     },
#     "embedding_similarity": {
#         "name": "embedding_similarity",
#         "description": "description",
#         "parameters": {
#             "type": "object",
#             "properties": {
#                 "text": {
#                     "type": "string",
#                     "description": "The text to extract the data from",
#                 }
#             },
#             "required": ["text"],
#         },
#     },
#     "vector_databases": {
#         "name": "vector_databases",
#         "description": "description",
#         "parameters": {
#             "type": "object",
#             "properties": {
#                 "text": {
#                     "type": "string",
#                     "description": "The text to extract the data from",
#                 }
#             },
#             "required": ["text"],
#         },
#     },
#     "function_calling": {
#         "name": "function_calling",
#         "description": "description",
#         "parameters": {
#             "type": "object",
#             "properties": {
#                 "text": {
#                     "type": "string",
#                     "description": "The text to extract the data from",
#                 }
#             },
#             "required": ["text"],
#         },
#     },
#     "get_an_llm_to_say_yes": {
#         "name": "get_an_llm_to_say_yes",
#         "description": "description",
#         "parameters": {
#             "type": "object",
#             "properties": {
#                 "text": {
#                     "type": "string",
#                     "description": "The text to extract the data from",
#                 }
#             },
#             "required": ["text"],
#         },
#     },
#     "import_html_to_google_sheets": {
#         "name": "import_html_to_google_sheets",
#         "description": "description",
#         "parameters": {
#             "type": "object",
#             "properties": {
#                 "text": {
#                     "type": "string",
#                     "description": "The text to extract the data from",
#                 }
#             },
#             "required": ["text"],
#         },
#     },
#     "scrape_imdb_movies": {
#         "name": "scrape_imdb_movies",
#         "description": "description",
#         "parameters": {
#             "type": "object",
#             "properties": {
#                 "text": {
#                     "type": "string",
#                     "description": "The text to extract the data from",
#                 }
#             },
#             "required": ["text"],
#         },
#     },
#     "wikipedia_outline": {
#         "name": "wikipedia_outline",
#         "description": "description",
#         "parameters": {
#             "type": "object",
#             "properties": {
#                 "text": {
#                     "type": "string",
#                     "description": "The text to extract the data from",
#                 }
#             },
#             "required": ["text"],
#         },
#     },
#     "scrape_the_bbc_weather_api": {
#         "name": "scrape_the_bbc_weather_api",
#         "description": "description",
#         "parameters": {
#             "type": "object",
#             "properties": {
#                 "text": {
#                     "type": "string",
#                     "description": "The text to extract the data from",
#                 }
#             },
#             "required": ["text"],
#         },
#     },
#     "find_the_bounding_box_of_a_city": {
#         "name": "find_the_bounding_box_of_a_city",
#         "description": "description",
#         "parameters": {
#             "type": "object",
#             "properties": {
#                 "text": {
#                     "type": "string",
#                     "description": "The text to extract the data from",
#                 }
#             },
#             "required": ["text"],
#         },
#     },
#     "search_hacker_news": {
#         "name": "search_hacker_news",
#         "description": "description",
#         "parameters": {
#             "type": "object",
#             "properties": {
#                 "text": {
#                     "type": "string",
#                     "description": "The text to extract the data from",
#                 }
#             },
#             "required": ["text"],
#         },
#     },
#     "find_newest_github_user": {
#         "name": "find_newest_github_user",
#         "description": "description",
#         "parameters": {
#             "type": "object",
#             "properties": {
#                 "text": {
#                     "type": "string",
#                     "description": "The text to extract the data from",
#                 }
#             },
#             "required": ["text"],
#         },
#     },
#     "create_a_scheduled_github_action": {
#         "name": "create_a_scheduled_github_action",
#         "description": "description",
#         "parameters": {
#             "type": "object",
#             "properties": {
#                 "text": {
#                     "type": "string",
#                     "description": "The text to extract the data from",
#                 }
#             },
#             "required": ["text"],
#         },
#     },
#     "extract_tables_from_pdf": {
#         "name": "extract_tables_from_pdf",
#         "description": "description",
#         "parameters": {
#             "type": "object",
#             "properties": {
#                 "text": {
#                     "type": "string",
#                     "description": "The text to extract the data from",
#                 }
#             },
#             "required": ["text"],
#         },
#     },
#     "convert_a_pdf_to_markdown": {
#         "name": "convert_a_pdf_to_markdown",
#         "description": "description",
#         "parameters": {
#             "type": "object",
#             "properties": {
#                 "text": {
#                     "type": "string",
#                     "description": "The text to extract the data from",
#                 }
#             },
#             "required": ["text"],
#         },
#     },
#     "clean_up_excel_sales_data": {
#         "name": "clean_up_excel_sales_data",
#         "description": "description",
#         "parameters": {
#             "type": "object",
#             "properties": {
#                 "text": {
#                     "type": "string",
#                     "description": "The text to extract the data from",
#                 }
#             },
#             "required": ["text"],
#         },
#     },
#     "clean_up_student_marks": {
#         "type": "function",
#         "function": {
#             "name": "clean_up_student_marks",
#             "description": "Analyzes logs to count the number of successful GET requests matching criteria such as URL prefix, weekday, time window, month, and year.",
#             "parameters": {
#                 "type": "object",
#                 "properties": {
#                     "file_path": {
#                         "type": "string",
#                         "description": "Path to the gzipped log file.",
#                     },
#                     "section_prefix": {
#                         "type": "string",
#                         "description": "URL prefix to filter log entries (e.g., '/telugu/').",
#                     },
#                     "weekday": {
#                         "type": "integer",
#                         "description": "Day of the week as an integer (0=Monday, ..., 6=Sunday).",
#                     },
#                     "start_hour": {
#                         "type": "integer",
#                         "description": "Start hour (inclusive) in 24-hour format.",
#                     },
#                     "end_hour": {
#                         "type": "integer",
#                         "description": "End hour (exclusive) in 24-hour format.",
#                     },
#                     "month": {
#                         "type": "integer",
#                         "description": "Month number (e.g., 5 for May).",
#                     },
#                     "year": {"type": "integer", "description": "Year (e.g., 2024)."},
#                 },
#                 "required": [
#                     "file_path",
#                     "section_prefix",
#                     "weekday",
#                     "start_hour",
#                     "end_hour",
#                     "month",
#                     "year",
#                 ],
#             },
#         },
#     },
#     "apache_log_downloads": {
#         "name": "apache_log_downloads",
#         "description": "description",
#         "parameters": {
#             "type": "object",
#             "properties": {
#                 "text": {
#                     "type": "string",
#                     "description": "The text to extract the data from",
#                 }
#             },
#             "required": ["text"],
#         },
#     },
#     "clean_up_sales_data": {
#         "name": "clean_up_sales_data",
#         "description": "description",
#         "parameters": {
#             "type": "object",
#             "properties": {
#                 "text": {
#                     "type": "string",
#                     "description": "The text to extract the data from",
#                 }
#             },
#             "required": ["text"],
#         },
#     },
#     "parse_partial_json": {
#         "name": "parse_partial_json",
#         "description": "description",
#         "parameters": {
#             "type": "object",
#             "properties": {
#                 "text": {
#                     "type": "string",
#                     "description": "The text to extract the data from",
#                 }
#             },
#             "required": ["text"],
#         },
#     },
#     "extract_nested_json_keys": {
#         "name": "extract_nested_json_keys",
#         "description": "description",
#         "parameters": {
#             "type": "object",
#             "properties": {
#                 "text": {
#                     "type": "string",
#                     "description": "The text to extract the data from",
#                 }
#             },
#             "required": ["text"],
#         },
#     },
#     "duckdb_social_media_interactions": {
#         "name": "duckdb_social_media_interactions",
#         "description": "description",
#         "parameters": {
#             "type": "object",
#             "properties": {
#                 "text": {
#                     "type": "string",
#                     "description": "The text to extract the data from",
#                 }
#             },
#             "required": ["text"],
#         },
#     },
#     "transcribe_a_youtube_video": {
#         "name": "transcribe_a_youtube_video",
#         "description": "description",
#         "parameters": {
#             "type": "object",
#             "properties": {
#                 "text": {
#                     "type": "string",
#                     "description": "The text to extract the data from",
#                 }
#             },
#             "required": ["text"],
#         },
#     },
#     "reconstruct_an_image": {
#         "name": "reconstruct_an_image",
#         "description": "description",
#         "parameters": {
#             "type": "object",
#             "properties": {
#                 "text": {
#                     "type": "string",
#                     "description": "The text to extract the data from",
#                 }
#             },
#             "required": ["text"],
#         },
#     },
# }




function_definitions_objects_llm = {
    "vs_code_version": {
        "name": "vs_code_version",
        "description": "description",
        "parameters": {
            "type": "object",
            "properties": {
                "text": {}
            },
            "required": []
        }
    },

    "make_http_requests_with_uv": {
        "name": "make_http_requests_with_uv",
        "description": "Extract the URL and query parameters from a question about making HTTP requests with UV, then perform the request and return results.",
        "parameters": {
            "type": "object",
            "properties": {
                "query_params": {
                    "type": "object",
                    "description": "The query parameters to send with the request URL encoded parameters"
                },
                "url": {
                    "type": "string",
                    "description": "The URL to make the request to"
                }
            },
            "required": ["query_params", "url"]
        }
    },

    "run_command_with_npx": {
        "name": "run_command_with_npx",
        "description": "Runs Prettier (version 3.4.2) on an input file and returns the SHA-256 hash of the formatted content. The function handles the file processing internally. Returns output in sha256sum format (hash followed by ' -').",
        "parameters": {
            "type": "object",
            "properties": {
                "prettier_version": {
                    "type": "string",
                    "description": "Version of Prettier to use",
                    "default": "3.4.2"
                }
            },
            "required": []
        }
    },

    "use_google_sheets": {
        "name": "use_google_sheets",
        "description": "Simulates Google Sheets' SEQUENCE and ARRAY_CONSTRAIN functions to calculate the sum of a constrained array. This function creates a matrix with specified dimensions starting with a specific value and incrementing by a step value, then extracts a portion of that matrix and calculates the sum.",
        "parameters": {
            "type": "object",
            "properties": {
                "rows": {
                    "type": "integer",
                    "description": "Number of rows in the matrix (default: 100)"
                },
                "cols": {
                    "type": "integer",
                    "description": "Number of columns in the matrix (default: 100)"
                },
                "start": {
                    "type": "integer",
                    "description": "Starting value of the sequence (default: 5)"
                },
                "step": {
                    "type": "integer",
                    "description": "Increment value between elements (default: 4)"
                },
                "extract_rows": {
                    "type": "integer",
                    "description": "Number of rows to extract for the constrained array (default: 1)"
                },
                "extract_cols": {
                    "type": "integer",
                    "description": "Number of columns to extract for the constrained array (default: 10)"
                }
            },
            "required": []
        }
    },

    "use_excel": {
        "name": "use_excel",
        "description": "Simulates Excel's SORTBY and TAKE functions followed by SUM. This function sorts an array of values based on sort keys, extracts a specified number of elements from the beginning of the sorted array, and calculates their sum.",
        "parameters": {
            "type": "object",
            "properties": {
                "values": {
                    "type": "array",
                    "items": {"type": "number"},
                    "description": "Array of numeric values to be sorted (default: [13, 12, 0, 14, 2, 12, 9, 15, 1, 7, 3, 10, 9, 15, 2, 0])"
                },
                "sort_keys": {
                    "type": "array",
                    "items": {"type": "number"},
                    "description": "Array of keys used to sort the values array (default: [10, 9, 13, 2, 11, 8, 16, 14, 7, 15, 5, 4, 6, 1, 3, 12])"
                },
                "num_rows": {
                    "type": "integer",
                    "description": "Number of rows to extract (used in TAKE function, similar to first parameter) (default: 1)"
                },
                "num_elements": {
                    "type": "integer",
                    "description": "Number of elements to sum from the beginning of the sorted array (default: 9)"
                }
            },
            "required": []
        }
    },

    "use_devtools": {
        "name": "use_devtools",
        "description": "Extracts the value from a hidden input field in HTML content. The hidden input is typically of type 'hidden' and contains a secret value that needs to be retrieved.",
        "parameters": {
            "type": "object",
            "properties": {
                "hiddenvalue": {
                    "type": "string",
                    "description": "The value in the hidden element"
                }
            },
            "required": []
        }
    },

    "count_wednesdays": {
        "name": "count_wednesdays",
        "description": "Count the number of specific weekdays between two dates",
        "parameters": {
            "type": "object",
            "properties": {
                "start_date": {
                    "type": "string",
                    "description": "Start date in YYYY-MM-DD format"
                },
                "end_date": {
                    "type": "string",
                    "description": "End date in YYYY-MM-DD format"
                },
                "weekday": {
                    "type": "integer",
                    "description": "Day of week to count (0=Monday, 1=Tuesday, 2=Wednesday, etc.)"
                }
            },
            "required": ["start_date", "end_date"]
        }
    },

    "extract_csv_from_a_zip": {
        "name": "extract_csv_from_a_zip",
        "description": "Extract a CSV file from a ZIP archive and return values from a specific column",
        "parameters": {
            "type": "object",
            "properties": {
                "zip_path": {
                    "type": "string",
                    "description": "Path to the ZIP file containing the CSV file"
                },
                "extract_to": {
                    "type": "string",
                    "description": "Directory to extract files to (default: 'extracted_files')"
                },
                "csv_filename": {
                    "type": "string",
                    "description": "Name of the CSV file to extract (default: 'extract.csv')"
                },
                "column_name": {
                    "type": "string",
                    "description": "Name of the column to extract values from (default: 'answer')"
                }
            },
            "required": ["zip_path"]
        }
    },

    "use_json": {
        "name": "use_json",
        "description": "description",
        "parameters": {
            "type": "object",
            "properties": {
                "input_data": {
                    "type": "string",
                    "description": "The text to extract the data from"
                }
            },
            "required": ["input_data"]
        }
    },

    "multi_cursor_edits_to_convert_to_json": {
        "name": "multi_cursor_edits_to_convert_to_json",
        "description": "Converts a multi-line text file containing key=value pairs into a JSON object. Each line in the file should have a single key=value pair, which gets transformed into a key-value pair in the resulting JSON object.",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path to the text file containing key=value pairs, one per line"
                }
            },
            "required": ["file_path"]
        }
    },

    "css_selectors": {
        "name": "css_selectors",
        "description": "description",
        "parameters": {
            "type": "object",
            "properties": {},
            "required": []
        }
    },

    "process_files_with_different_encodings": {
        "name": "process_files_with_different_encodings",
        "description": "Process files with different encodings and sum values associated with specific symbols",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path to the zip file containing files with different encodings (data1.csv in CP-1252, data2.csv in UTF-8, data3.txt in UTF-16)"
                }
            },
            "required": []
        }
    },

    "use_github": {
        "name": "use_github",
        "description": "deos something in github for which the email or the parameter in given in the question is required that needs to be included",
        "parameters": {
            "type": "object",
            "properties": {
                "new_email": {
                    "type": "string",
                    "description": "the parameter or the email that is given in the question"
                }
            },
            "required": []
        }
    },

    "replace_across_files": {
        "name": "replace_across_files",
        "description": "Download and extract a zip file, replace 'IITM' (case-insensitive) with 'IIT Madras' in all files, and calculate a hash of the result",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path to the zip file containing the files to process"
                }
            },
            "required": ["file_path"]
        }
    },

    "list_files_and_attributes": {
        "name": "list_files_and_attributes",
        "description": "Download and extract a zip file, then list all files with their dates and sizes, calculating the total size of files meeting specific criteria",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path to the zip file containing the files to process"
                },
                "min_size": {
                    "type": "integer",
                    "description": "Minimum file size in bytes (default: 6262)"
                },
                "reference_date": {
                    "type": "string",
                    "description": "Reference date in format 'YYYY-MM-DD HH:MM:SS' (default: '2019-03-22 14:31:00')"
                },
                "timezone": {
                    "type": "string",
                    "description": "Timezone for reference date (default: 'Asia/Kolkata')"
                },
                "debug": {
                    "type": "boolean",
                    "description": "Whether to print debug information (default: False)"
                }
            },
            "required": ["file_path"]
        }
    },

    "compare_files": {
        "name": "compare_files",
        "description": "Compare two files and analyze differences",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path to the zip file containing files to compare"
                }
            },
            "required": ["file_path"]
        }
    },

    "sql_ticket_sales": {
        "name": "sql_ticket_sales",
        "description": "description",
        "parameters": {
            "type": "object",
            "properties": {},
            "required": []
        }
    },

    "write_documentation_in_markdown": {
        "name": "write_documentation_in_markdown",
        "description": "description",
        "parameters": {
            "type": "object",
            "properties": {},
            "required": []
        }
    },

    "compress_an_image": {
        "name": "compress_an_image",
        "description": "Compress an image to be under 1,500 bytes and return it as base64",
        "parameters": {
            "type": "object",
            "properties": {
                "image_path": {
                    "type": "string",
                    "description": "Path to the image file to compress"
                }
            },
            "required": ["image_path"]
        }
    },

    "host_your_portfolio_on_github_pages": {
        "name": "host_your_portfolio_on_github_pages",
        "description": "deos something in github for which the email or the parameter in given in the question is required that needs to be included in the pages site portfolio",
        "parameters": {
            "type": "object",
            "properties": {
                "new_email": {
                    "type": "string",
                    "description": "the parameter or the email that is given in the question"
                }
            },
            "required": []
        }
    },

    "use_google_colab": {
        "name": "use_google_colab",
        "description": "Extract the email to get the result of running hashlib code in Google Colab",
        "parameters": {
            "type": "object",
            "properties": {
                "email": {
                    "type": "string",
                    "description": "The email address to use with Google Colab"
                }
            },
            "required": ["email"]
        }
    },

    "use_an_image_library_in_google_colab": {
        "name": "use_an_image_library_in_google_colab",
        "description": "Processes an image to count pixels with brightness above a threshold (0.683). This function opens the image, converts it to RGB format if needed, calculates lightness values using the HLS color model, and counts pixels exceeding the threshold.",
        "parameters": {
            "type": "object",
            "properties": {
                "image_path": {
                    "type": "string",
                    "description": "Path to the image file to process. If not provided, the function will search for images in common upload locations."
                }
            },
            "required": []
        }
    },

    "deploy_a_python_api_to_vercel": {
        "name": "deploy_a_python_api_to_vercel",
        "description": "description",
        "parameters": {
            "type": "object",
            "properties": {},
            "required": []
        }
    },

    "create_a_github_action": {
        "name": "create_a_github_action",
        "description": "Create a scheduled GitHub action that runs daily and adds a commit to your repository.",
        "parameters": {
            "type": "object",
            "properties": {
                "new_email": {
                    "type": "string",
                    "description": "The email address to configure in the GitHub workflow. It is not necessarily a email but can be any string or parameter. It will be a parameter after text 'Include a step with your' and end with 'in its name' "
                },
                "cron": {
                    "type": "string",
                    "description": "The cron syntax for scheduling the workflow (e.g., '30 2 * * *')."
                }
            },
            "required": ["new_email"]
        }
    },

    "push_an_image_to_docker_hub": {
        "name": "push_an_image_to_docker_hub",
        "description": "Creates and pushes a Docker image to Docker Hub with the specified tag. Uses environment variables for authentication.",
        "parameters": {
            "type": "object",
            "properties": {
                "new_tag": {
                    "type": "string",
                    "description": "the tag required for the docker image"
                }
            },
            "required": []
        }
    },

    "write_a_fastapi_server_to_serve_data": {
        "name": "write_a_fastapi_server_to_serve_data",
        "description": "Creates and runs a FastAPI application that serves student data from a CSV file with filtering capabilities by class",
        "parameters": {
            "type": "object",
            "properties": {
                "csv_path": {
                    "type": "string",
                    "description": "Path to the CSV file containing student data. The CSV must have a 'class' column among other student data."
                },
                "host": {
                    "type": "string",
                    "description": "The host address to run the API on (e.g., '127.0.0.1', '0.0.0.0')",
                    "default": "127.0.0.1"
                },
                "port": {
                    "type": "integer",
                    "description": "The port number to run the API on (e.g., 8000, 8080)",
                    "default": 8000
                }
            },
            "required": ["csv_path"]
        }
    },

    "run_a_local_llm_with_llamafile": {
        "name": "run_a_local_llm_with_llamafile",
        "description": "description",
        "parameters": {
            "type": "object",
            "properties": {
                "text": {
                    "type": "string",
                    "description": "The text to extract the data from"
                }
            },
            "required": ["text"]
        }
    },

    "llm_sentiment_analysis": {
        "name": "llm_sentiment_analysis",
        "description": "Analyzes the sentiment of provided text using OpenAI's API, categorizing it as GOOD, BAD, or NEUTRAL. This function makes a request to the OpenAI API with the specified text and returns the sentiment analysis result.",
        "parameters": {
            "type": "object",
            "properties": {
                "text": {
                    "type": "string",
                    "description": "The text content to analyze for sentiment. If empty, will return an analysis of empty text."
                }
            },
            "required": ["text"]
        }
    },

    "llm_token_cost": {
        "name": "llm_token_cost",
        "description": "Calculate the token count for text using OpenAI's GPT-4o-Mini model. This function sends the text to OpenAI's API and extracts the prompt token count from the response, which represents how many tokens the input text consumes.",
        "parameters": {
            "type": "object",
            "properties": {
                "text": {
                    "type": "string",
                    "description": "The text content to analyze for token count. If not provided, defaults to an empty string."
                }
            },
            "required": []
        }
    },

    "generate_addresses_with_llms": {
        "name": "generate_addresses_with_llms",
        "description": "Creates a JSON request body for OpenAI API to generate structured address data. This function prepares a properly formatted request that will instruct the language model to generate realistic addresses for logistics and delivery route planning.",
        "parameters": {
            "type": "object",
            "properties": {
                "model": {
                    "type": "string",
                    "description": "The OpenAI model to use for generating addresses. Default is 'gpt-4o-mini'.",
                    "default": "gpt-4o-mini"
                },
                "count": {
                    "type": "integer",
                    "description": "Number of addresses to generate. Default is 10.",
                    "default": 10
                },
                "system_message": {
                    "type": "string",
                    "description": "System prompt instruction for the model. Default is 'Respond in JSON'.",
                    "default": "Respond in JSON"
                },
                "country": {
                    "type": "string",
                    "description": "Country to generate addresses for. Default is 'US'.",
                    "default": "US"
                }
            },
            "required": []
        }
    },

    "llm_vision": {
        "name": "llm_vision",
        "description": "Generate a JSON body for an OpenAI vision API request to analyze images. This function formats the request with a text prompt and an image URL, creating the proper structure required by OpenAI's API for combined text-and-image inputs.",
        "parameters": {
            "type": "object",
            "properties": {
                "image_url": {
                    "type": "string",
                    "description": "URL to the image to be analyzed (can be a web URL or base64 data URL)."
                },
                "model": {
                    "type": "string",
                    "description": "The OpenAI model to use for vision processing. Default is 'gpt-4o-mini'."
                },
                "prompt": {
                    "type": "string",
                    "description": "The instruction to send to the model, such as 'Extract text from this image'. Default is 'Extract text from this image'."
                }
            },
            "required": ["image_url"]
        }
    },

    "llm_embeddings": {
        "name": "llm_embeddings",
        "description": "Generate a JSON body for an OpenAI embeddings API request using the text-embedding-3-small model.",
        "parameters": {
            "type": "object",
            "properties": {
                "model": {"type": "string", "enum": ["text-embedding-3-small"], "description": "The OpenAI model to use for generating text embeddings."},
                "input_texts": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "List of text strings to generate embeddings for."
                }
            },
            "required": ["model", "input_texts"]
        }
    },

    "embedding_similarity": {
        "name": "embedding_similarity",
        "description": "Calculate cosine similarity between embeddings and return the most similar pair.",
        "parameters": {
            "type": "object",
            "properties": {},
            "required": []
        }
    },

    "vector_databases": {
        "name": "vector_databases",
        "description": "Creates and runs a FastAPI application that provides a semantic search API using vector embeddings. This function sets up an endpoint that accepts document texts and a query, calculates similarity using text embeddings, and returns the most similar documents.",
        "parameters": {
            "type": "object",
            "properties": {
                "host": {
                    "type": "string",
                    "description": "The host address to run the API on (default: '127.0.0.1')"
                },
                "port": {
                    "type": "integer",
                    "description": "The port number to run the API on (default: 8000)"
                }
            },
            "required": []
        }
    },

    "function_calling": {
        "name": "function_calling",
        "description": "Creates and runs a FastAPI application that processes natural language queries and converts them into structured API calls for various operations like checking ticket status, scheduling meetings, retrieving expense balances, calculating performance bonuses, and reporting office issues.",
        "parameters": {
            "type": "object",
            "properties": {
                "host": {
                    "type": "string",
                    "description": "The host address to run the API on (default: '127.0.0.1')"
                },
                "port": {
                    "type": "integer",
                    "description": "The port number to run the API on (default: 8000)"
                }
            },
            "required": []
        }
    },

    "get_an_llm_to_say_yes": {
        "name": "get_an_llm_to_say_yes",
        "description": "description",
        "parameters": {
            "type": "object",
            "properties": {},
            "required": []
        }
    },

    "import_html_to_google_sheets": {
        "name": "import_html_to_google_sheets",
        "description": "Scrapes the third table with caption 'Overall figures' from an ESPN Cricinfo ODI batting stats page and returns the total number of ducks (scores of 0) from that table. The page number is parameterized.",
        "parameters": {
            "type": "object",
            "properties": {
                "page_number": {
                    "type": "integer",
                    "description": "The page number of the ESPN Cricinfo ODI batting stats to scrape (e.g., 23). Must be a positive integer."
                }
            },
            "required": ["page_number"]
        }
    },

    "scrape_imdb_movies": {
        "name": "scrape_imdb_movies",
        "description": "Fetches movie titles from IMDb within a specified rating range",
        "parameters": {
            "type": "object",
            "properties": {
                "min_rating": {
                    "type": "number",
                    "description": "Minimum IMDb rating (0-10)"
                },
                "max_rating": {
                    "type": "number",
                    "description": "Maximum IMDb rating (0-10)"
                }
            },
            "required": ["min_rating", "max_rating"]
        }
    },

    "wikipedia_outline": {
        "name": "wikipedia_outline",
        "description": "Creates and runs a FastAPI application that provides a Wikipedia outline API on localhost",
        "parameters": {
            "type": "object",
            "properties": {
                "host": {
                    "type": "string",
                    "description": "The host address to run the API on (default: '127.0.0.1')"
                },
                "port": {
                    "type": "integer",
                    "description": "The port number to run the API on (default: 8000)"
                },
                "enable_cors": {
                    "type": "boolean",
                    "description": "Whether to enable CORS for all origins (default: True)"
                }
            },
            "required": []
        }
    },

    "scrape_the_bbc_weather_api": {
        "name": "scrape_the_bbc_weather_api",
        "type": "function",
        "description": "Fetches and scrapes weather forecast data...",
        "parameters": {
            "type": "object",
            "properties": {
                "city": {
                    "type": "string",
                    "description": "The name of the city for which to retrieve the weather forecast..."
                }
            },
            "required": ["city"]
        }
    },

    "find_the_bounding_box_of_a_city": {
        "name": "find_the_bounding_box_of_a_city",
        "description": "Retrieves the minimum or maximum latitude of the bounding box for a specified city using geocoding",
        "parameters": {
            "type": "object",
            "properties": {
                "city_name": {
                    "type": "string",
                    "description": "The name of the city to geocode (e.g., 'Mexico City', 'New York', 'Tokyo')"
                },
                "bound_type": {
                    "type": "string",
                    "description": "Type of boundary to return - 'minimum' or 'maximum'",
                    "enum": ["minimum", "maximum"]
                },
                "osm_id_ending": {
                    "type": "string",
                    "description": "The ending pattern of the osm_id to match (e.g., \"2077\")"
                }
            },
            "required": ["city_name", "bound_type"]
        }
    },

    "search_hacker_news": {
        "name": "search_hacker_news",
        "description": "Searches Hacker News via the HNRSS API for the latest post mentioning a specified technology topic with a minimum number of points, returning the post's link as a JSON object.",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "The technology topic to search for in Hacker News posts (e.g., 'python', 'blockchain')."
                },
                "points": {
                    "type": "integer",
                    "description": "The minimum number of points the post must have to be considered relevant."
                }
            },
            "required": ["query", "points"]
        }
    },

    "find_newest_github_user": {
        "name": "find_newest_github_user",
        "description": "Searches GitHub for the newest user in a specified location with a follower count based on a comparison operator, excluding users who joined after March 23, 2025, 3:57:03 PM PDT. Returns the creation date in ISO 8601 format.",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {
                    "type": "string",
                    "description": "The city to search for GitHub users (e.g., 'Delhi')."
                },
                "followers": {
                    "type": "integer",
                    "description": "The number of followers to filter by."
                },
                "operator": {
                    "type": "string",
                    "enum": ["gt", "lt", "eq"],
                    "description": "The comparison operator for followers: 'gt' for greater than, 'lt' for less than, 'eq' for equal to."
                }
            },
            "required": ["location", "followers", "operator"]
        }
    },

    "create_a_scheduled_github_action": {
        "name": "create_a_scheduled_github_action",
        "description": "Create a scheduled GitHub action that runs daily and adds a commit to your repository.",
        "parameters": {
            "type": "object",
            "properties": {
                "email": {
                    "type": "string",
                    "description": "The email address to configure in the GitHub workflow. It is not necessarily a email but can be any string or parameter. It will be a parameter after text 'Include a step with your' and end with 'in its name' "
                },
                "cron": {
                    "type": "string",
                    "description": "The cron syntax for scheduling the workflow (e.g., '30 2 * * *')."
                }
            },
            "required": ["email"]
        }
    },

    "extract_tables_from_pdf": {
        "name": "extract_tables_from_pdf",
        "description": "Calculate total marks for one subject for students meeting score criteria in another subject within specified groups from a PDF file containing student marks.",
        "parameters": {
            "type": "object",
            "properties": {
                "pdf_path": {
                    "type": "string",
                    "description": "Path to the PDF file containing student marks data organized by groups"
                },
                "filter_subject": {
                    "type": "string",
                    "description": "Subject name to filter by (e.g., 'English', 'Economics')"
                },
                "min_score": {
                    "type": "integer",
                    "description": "Minimum score threshold for the filter subject"
                },
                "sum_subject": {
                    "type": "string",
                    "description": "Subject name to sum marks for (e.g., 'Maths', 'Biology')"
                },
                "start_group": {
                    "type": "integer",
                    "description": "Starting group number (inclusive) to include in the calculation"
                },
                "end_group": {
                    "type": "integer",
                    "description": "Ending group number (inclusive) to include in the calculation"
                }
            },
            "required": ["pdf_path", "filter_subject", "min_score", "sum_subject", "start_group", "end_group"]
        }
    },

    "convert_a_pdf_to_markdown": {
        "name": "convert_a_pdf_to_markdown",
        "description": "Converts a PDF file to Markdown format and applies Prettier formatting. This function extracts text content from a PDF, preserving structure when possible, and formats it using Prettier version 3.4.2 for consistent styling.",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path to the PDF file to convert. If not provided, the function will attempt to find a PDF file in common upload locations."
                }
            },
            "required": []
        }
    },

    "clean_up_excel_sales_data": {
        "name": "clean_up_excel_sales_data",
        "description": "Cleans messy sales data from Excel files and calculates margins for filtered transactions. This function standardizes country codes, normalizes text fields, handles date format inconsistencies, extracts product names from compound fields, and calculates sales margins for transactions matching specified criteria.",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path to the Excel file containing sales data. If not provided, the function will search for Excel files in common locations."
                },
                "cutoff_date": {
                    "type": "string",
                    "description": "ISO 8601 date string to filter transactions (inclusive). Only transactions on or before this date will be included.",
                    "default": "2022-11-24T11:42:27+05:30"
                },
                "product_name": {
                    "type": "string",
                    "description": "Product name to filter by. For compound product fields with slashes, only the part before the slash is used.",
                    "default": "Kappa"
                },
                "country_code": {
                    "type": "string",
                    "description": "Country code to filter by after standardization (e.g., 'BR', 'US'). The function standardizes various country formats to consistent codes.",
                    "default": "BR"
                }
            },
            "required": []
        }
    },

    "clean_up_student_marks": {
        "name": "clean_up_student_marks",
        "description": "Counts the number of unique student IDs in a text file. Each student ID is exactly 10 characters long and consists of uppercase letters and/or numbers.",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path to the text file containing student IDs"
                }
            },
            "required": ["file_path"]
        }
    },

    "apache_log_requests": {
        "name": "apache_log_requests",
        "description": "Extracts and analyzes Apache log requests for specific conditions, such as peak usage periods, request types, and success criteria.",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "The file path of the GZipped Apache log file."
                },
                "topic_heading": {
                    "type": "string",
                    "description": "A short heading summarizing the analysis topic."
                },
                "start_time": {
                    "type": "string",
                    "description": "The start time of the time window for analysis, in HH format (24-hour)."
                },
                "end_time": {
                    "type": "string",
                    "description": "The end time (exclusive) of the time window for analysis, in HH format (24-hour)."
                },
                "day": {
                    "type": "string",
                    "description": "The specific day for analysis (e.g., 'Sunday')."
                }
            },
            "required": ["file_path", "topic_heading", "start_time", "end_time", "day"]
        }
    },

    "apache_log_downloads": {
        "name": "apache_log_downloads",
        "description": "Analyzes an Apache log file to track bandwidth usage for a specific station and date. The function filters log entries based on a given date and extracts only those requests related to a specific station. It then aggregates data by IP address, calculating the total bytes downloaded per IP. Finally, it identifies the top data-consuming IP and reports the total bytes downloaded by that IP.",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "The full file path of the Apache log file (GZipped format)."
                },
                "station_name": {
                    "type": "string",
                    "description": "The name of the station or content category being analyzed (e.g., 'tamilmp3')."
                },
                "date": {
                    "type": "string",
                    "format": "date",
                    "description": "The specific date (YYYY-MM-DD) for which log entries should be filtered."
                }
            },
            "required": ["file_path", "station_name", "date"]
        }
    },

    "clean_up_sales_data": {
        "name": "clean_up_sales_data",
        "description": "Clean up the sales data given in the json file. To do this, find the product, city and minimum units (min_units) asked for in the question",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "The JSON file containing product data."
                },
                "product": {
                    "type": "string",
                    "description": "The product for which we want to find the number of units sold in a given city and minimum order quantity per transaction"
                },
                "city": {
                    "type": "string",
                    "description": "The city for which we want to find the number of units sold in a given product and minimum order quantity per transaction"
                },
                "min_units": {
                    "type": "number",
                    "description": "The minimum units of the product per transaction for which we want to find the number of units sold in a given city."
                }
            },
            "required": ["file_path", "product", "city", "min_units"]
        }
    },

    "parse_partial_json": {
        "name": "parse_partial_json",
        "description": "Aggregates the numeric values of a specified key from a JSONL file and returns the total sum. This function is intended for processing digitized OCR data from sales receipts, where some entries may be truncated. It extracts the numeric value from each row based on the provided key and a regular expression pattern, validates the data, and computes the aggregate sum.",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "The path to the JSONL file containing the digitized sales data."
                },
                "key": {
                    "type": "string",
                    "description": "The JSON key whose numeric values will be summed (e.g., 'sales')."
                },
                "num_rows": {
                    "type": "integer",
                    "description": "The total number of rows in the JSONL file for data validation purposes."
                },
                "regex_pattern": {
                    "type": "string",
                    "description": "A custom regular expression pattern to extract the numeric value from each JSON line."
                }
            },
            "required": ["file_path", "key", "num_rows", "regex_pattern"]
        }
    },

    "extract_nested_json_keys": {
        "name": "extract_nested_json_keys",
        "description": "Counts the number of times a specific key appears in a nested JSON structure, traversing through all objects and arrays recursively. Used to analyze large log files for system events or errors.",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path to the JSON file to analyze. If not provided, uses a default name of 'nested_json.json'."
                },
                "target_key": {
                    "type": "string",
                    "description": "The key name to search for within the JSON structure (e.g., 'TQG'). Counts only occurrences as keys, not values.",
                    "default": "TQG"
                }
            },
            "required": []
        }
    },

    "duckdb_social_media_interactions": {
        "name": "duckdb_social_media_interactions",
        "description": "Write a DuckDB query to filter posts by date, evaluate comment quality, extract and sort the Post IDs according to the timestamp, number of comments, and number of useful stars on the posts.",
        "parameters": {
            "type": "object",
            "properties": {
                "Time": {
                    "type": "string",
                    "format": "date-time",
                    "description": "The timestamp after which the posts are to be filtered (ISO 8601 format)"
                },
                "Comments": {
                    "type": "integer",
                    "description": "The minimum number of comments on the posts to be filtered"
                },
                "Stars": {
                    "type": "integer",
                    "description": "The minimum number of useful stars on the posts to be filtered"
                }
            },
            "required": ["Time", "Comments", "Stars"]
        }
    },

    "transcribe_a_youtube_video": {
        "name": "transcribe_a_youtube_video",
        "description": "description",
        "parameters": {
            "type": "object",
            "properties": {
                "text": {
                    "type": "string",
                    "description": "The text to extract the data from"
                }
            },
            "required": ["text"]
        }
    },

    "reconstruct_an_image": {
        "name": "reconstruct_an_image",
        "description": "Reconstructs a jigsaw puzzle image using predefined mapping data and returns the result as a Base64 encoded string",
        "parameters": {
            "type": "object",
            "properties": {
                "scrambled_image_path": {
                    "type": "string",
                    "description": "Path to the scrambled jigsaw image file (supported formats: PNG, JPEG, WebP)"
                }
            },
            "required": ["scrambled_image_path"]
        }
    }
}