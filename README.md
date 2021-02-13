# speedtest-monitoring
Collects results from speedtest-cli and saves them to csv file for historical analysis

## setup
Download speedtest monitoring

Download https://raw.githubusercontent.com/sivel/speedtest-cli/master/speedtest.py and place it in the same directory

Set any speedtest-cli parameters (e.g. --no-download) in `speedtestParameters` variable. If down- or upload check is disabled, CSV export will contain 2 instead of 3 columns

## usage
Create cron job with a frequency of your choice

Results will be saved to `output.csv`