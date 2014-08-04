class USPSInterface(object):

    def identify(self, tracking_number):
        return tracking_number.startswith('91') or tracking_number.startswith('92')

    def url(self, tracking_number):
        return ('http://trkcnfrm1.smi.usps.com/PTSInternetWeb/'
                'InterLabelInquiry.do?origTrackNum=%s' % tracking_number)
