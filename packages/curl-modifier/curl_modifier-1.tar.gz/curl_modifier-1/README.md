# cURL Modifier

This is a simple module for modifying and/or repeatedly executing cURL requests. 

# Main Features

cURL requests can be repeated quickly by making use of parallel processing. 

Additionally, this module can be useful for security testing. You can dynamically replace a substring in the request with, for example, XSS vectors written in a pre-defined text file. These modified requests will also be executed.

# Typical Usage Examples

## Repeat requests in parallel

Call the `execute_repeated_request` function with a valid cURL request and a desired `n` number of repeats. By default, this function works in parallel. If this causes problems for your machine, a `False` flag can be passed to disable it.

#### Parallel requests in Windows

Due to the lack of pickling in Windows, if you want to repeat requests in parallel you have to call the function in your script as follows:

```python
import curl_modifier

if __name__ == '__main__':
	curl_modifier.execute_repeated_request(curl_request, n)
```

## Penetration testing

One use case of this script is to check if attack vectors, in this example XSS, can be reflected/persisted on a website (assuming you have authority to execute penetration tests). A POST example for placing a comment on a forum may look like this:

```curl "{HTTPS_URL}" -H "foo: bar" "cookie: foo=bar"  --data "comment=REPLACE_THIS"```

In this case, you want to pass this request to the `execute_requests_with_file_substrings` function and replace a given string (in this case `REPLACE_THIS`) with many different vectors. This function requires you to pass a full path to a  `.txt` file with separated lines, like this:

```html
<script>alert('XSS Vector 1')</script>
<IMG SRC=x onerror="alert('XSS Vector 2')">
```

Each of these lines will replace the specified substring and these modified requests will all be executed. After the job has finished, you can visit the website you are testing and assert whether any XSS is reflected and/or if the inputs are sanitised in any way.

# Installation

`pip install curl_modifier`

