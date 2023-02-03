<h1>User Guide</h1>
Welcome to the Micro Analytics Platform! This platform allows you to collect and track how users interact with your websites.

<h2>Getting Started</h2>
1. Clone the repository from GitHub to your local machine:

bash

git clone https://github.com/micro-analytics/platform.git

2. Navigate to the platform directory:

bash

cd platform

3. Install the required dependencies using pip:

pip install -r requirements.txt

4. Start the platform using the following command:

python app.py

5. Visit http://localhost:5000 in your web browser to access the platform.

<h2>Tracking Events</h2>
To track events on your website, you can send a POST request to the /track endpoint with the following JSON payload:


{
    "event_type": "pageview",
    "url": "https://example.com/home"
}
or


{
    "event_type": "click",
    "button": "About Us"
}

You can track two types of events: pageviews and clicks. The event_type field should be set to pageview for pageview events, and click for click events. The url field should be set to the URL of the page being viewed, and the button field should be set to the label of the button being clicked.

<h2>Viewing Reports</h2>
To view reports on the events you've tracked, simply visit the platform's homepage at http://localhost:5000. You can view the number of pageviews and clicks, and view charts of the data over time.

<h2>Configuration</h2>
You can configure the platform by editing the config.yml file. This file contains the configuration for the platform, including the database connection information, the port number, and the URL for the platform.

<h2>Troubleshooting</h2>
If you encounter any issues with the platform, please check the logs.txt file for any error messages. If you can't resolve the issue, please open an issue on GitHub or reach out to the maintainers for assistance.

<h2>Conclusion</h2>
We hope that this guide has been helpful in getting you started with the Micro Analytics Platform. If you have any questions or feedback, please don't hesitate to reach out.