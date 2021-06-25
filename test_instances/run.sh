start_time=$(date +%d-%m-%Y_%H:%M:%S)
python -m unittest -v
#python -m unittest -v 2> error_message/report_${start_time}.txt
#python locators/slack_alert.py ${start_time}
