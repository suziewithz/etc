import sys

track_num = str(sys.argv[1])

def get_website_for_usps(track_num):
    return 'https://tools.usps.com/go/TrackConfirmAction?qtc_tLabels1=' + track_num

def get_website_for_ups(track_num):
    return 'https://wwwapps.ups.com/etracking/tracking.cgi?TypeOfInquiryNumber=T&InquiryNumber1=' + track_num

def get_website_for_fedex(track_num):
    return 'https://www.fedex.com/fedextrack/?trknbr=' + track_num

def get_website_for_ontrac(track_num):
    return 'https://www.ontrac.com/trackingresults.asp?tracking_number=' + track_num

def get_website(track_num):
    if track_num.startswith('1Z'):
        return get_website_for_ups(track_num)

    if track_num.startswith('C'):
        return get_website_for_ontrac(track_num)

    if len(track_num) == 22:
        return get_website_for_usps(track_num)

    if len(track_num) == 12 or len(track_num) == 15:
        return get_website_for_fedex(track_num)
	return

website = get_website(track_num)

if sys.stdout.isatty():
    print(website)
else:
    sys.stdout.write(website)
