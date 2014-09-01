from main import Init, init_collection

init_report_statuses = Init('report_statuses', [{
    'key': 'new',
    'description': 'This report is not verified yet'
}, {
    'key': 'assigned',
    'description': 'This report has been assigned for verification'
}, {
    'key': 'dismissed',
    'description': ''
}, {
    'key': 'false',
    'description': 'This report has been proven to be false!'
}, {
    'key': 'verified',
    'description': 'This report has been verified'
}])

if __name__ == "__main__": init_collection(init_report_statuses)
