# DraftGPT
GPT that drafts a Root Cause Analysis (RCA) document with input from unstructured sources (e.g. Slack chat, document templates, and emails).

What we would like is a more formalized output with more detailed input and correct analysis, similar to the following Q&A with ChatGPT

## Online usage

Enter a working API key in the input field, change chatgpt-model in the dropdown menu and start the workflow.

![image](https://private-user-images.githubusercontent.com/33799767/321284424-f5e79f19-c456-4e55-979c-32c53bd53d83.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MTMxODQwODgsIm5iZiI6MTcxMzE4Mzc4OCwicGF0aCI6Ii8zMzc5OTc2Ny8zMjEyODQ0MjQtZjVlNzlmMTktYzQ1Ni00ZTU1LTk3OWMtMzJjNTNiZDUzZDgzLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDA0MTUlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwNDE1VDEyMjMwOFomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTVmYTRhNmE4MzdmNWEyN2YwMzEyZDhjMjA2NzU4MWQxMTg4ZDFjYTIyNGJjYjBiYzdiZWRkY2RhOTZkZjZjMzgmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.1x9vG2fypLbkgjduWGKb52M-iAJbBdMuWP0jnRjvsHU)


## Example usage
``python3 test_draftgpt.py``

## Example use case
User/Owner: "My EC2 instance in AWS is taking a very long time to respond on HTTP requests. What is the likely cause, is it the CPU, the storage, the RAM, or the network that is the root cause of the problem?"

## Example GPT response 
When diagnosing slow response times on an EC2 instance in AWS, there could be several potential causes, and it's essential to troubleshoot systematically to identify the root cause. Here's a breakdown of how each component could contribute to the issue:

CPU: If the CPU utilization is consistently high (close to 100%), it could indicate that the server is under heavy load, causing delays in processing HTTP requests. This might be due to resource-intensive applications running on the server or an insufficiently sized instance for the workload.

Storage: Slow storage performance can lead to delays in serving HTTP requests, especially if the application relies heavily on disk I/O. Check if there are any disk bottlenecks, such as high disk queue lengths or elevated disk read/write latency. This could indicate that the storage subsystem (EBS volumes, instance store, etc.) is struggling to keep up with the demand.

RAM: Insufficient RAM can cause the server to rely on disk swapping, which significantly slows down performance. Monitor the memory utilization and swap usage on the instance. If the RAM is consistently maxed out and the swap usage is high, it could indicate a memory bottleneck.

Network: Network issues, such as high latency, packet loss, or limited bandwidth, can impact the responsiveness of HTTP requests. Use network monitoring tools to check for any network-related issues between the client and the EC2 instance, including network congestion or misconfigurations.

To determine the root cause, you can start by gathering performance metrics for each of these components using AWS CloudWatch or other monitoring tools. Look for any anomalies or patterns that correlate with the slow response times. Additionally, reviewing application logs and conducting load testing can help identify bottlenecks and performance issues within the application itself.

Once you've identified the likely culprit(s), you can take appropriate actions to address the issue, such as upgrading the instance type, optimizing the application code, scaling resources horizontally or vertically, or optimizing network configurations.
