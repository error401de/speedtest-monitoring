# speedtest-monitoring
Collects results from speedtest-cli and saves them to csv file for historical analysis

## setup
Download speedtest monitoring at https://raw.githubusercontent.com/error401de/speedtest-monitoring/main/speedtest-monitoring.py

Download https://raw.githubusercontent.com/sivel/speedtest-cli/master/speedtest.py and place it in the same directory

Make speedtest.py and speedtest-monitoring.py executable (`chmod +x filename`)

Set any speedtest-cli parameters (e.g. --no-download) in `speedtestParameters` variable. If down- or upload check is disabled, CSV export will contain 2 instead of 3 columns

## usage
Create cron job with a frequency of your choice

Results will be saved to `output.csv`