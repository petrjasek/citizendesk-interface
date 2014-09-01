from main import Init, init_collection

init_report_statuses = Init('report_statuses', [{
    'key': 'new',
    'direct': False,
    'description': 'This report is not verified yet'
}, {
    'key': 'assigned',
    'direct': False,
    'description': 'This report has been assigned for verification'
}, {
    'key': 'dismissed',
    'direct': True,
    'description': 'This report will not undergo verification'
}, {
    'key': 'false',
    'direct': True,
    'description': 'This report has been proven to be false!'
}, {
    'key': 'verified',
    'direct': True,
    'description': 'This report has been verified'
}])

if __name__ == "__main__": init_collection(init_report_statuses)
