# DraftGPT
GPT that drafts a Root Cause Analysis (RCA) document with input from unstructured sources (e.g. Slack chat, document templates, and emails).

What we would like is a more formalized output with more detailed input and correct analysis, similar to the following Q&A with ChatGPT

## Online usage

Enter a working API key in the input field, change chatgpt-model in the dropdown menu and start the workflow.

![image](https://i.imgur.com/2PjAUYL.png)


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
