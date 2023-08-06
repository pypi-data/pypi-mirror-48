class PsiturkException(Exception):
    def __init__(self, message='', **kwargs):
        super(PsiturkException, self).__init__(message)
        self.message=kwargs['message'] if 'message' in kwargs else ''
        
    def __str__(self):
        return '{}: {}'.format(type(self).__name__, self.message)


class AmtServicesWrapperError(PsiturkException):
    pass

class DoBonusError(AmtServicesWrapperError):
    def __init__(self, assignment_id='', **kwargs):
        super(DoBonusError, self).__init__(**kwargs)
        self.assignment_id = assignment_id


class AssignmentAlreadyBonusedError(DoBonusError):
    pass


class BadBonusAmountError(DoBonusError):
    def __init__(self, amount, **kwargs):
        super(BadBonusAmountError, self).__init__(**kwargs)
        self.message = 'Bonus must be a number greater than 0. You gave: {}'.format(
            amount)

class BonusReasonMissingError(DoBonusError):
    pass

class AssignmentIdNotFoundInLocalDBError(AmtServicesWrapperError):
    def __init__(self, assignment_id='', **kwargs):
        super(AssignmentIdNotFoundInLocalDBError, self).__init__(**kwargs)
        self.assignment_id = assignment_id
    
class WorkerIdNotFoundInLocalDBError(AmtServicesWrapperError):
    pass
    
class MissingArgumentsError(AmtServicesWrapperError):
    pass
    
class InvalidPsiturkCredentialsError(AmtServicesWrapperError):
    def __init__(self, *args, **kwargs):
        super(InvalidPsiturkCredentialsError, self).__init__(*args, **kwargs)
        self.message = '\n'.join(['*****************************',
            '  Sorry, your psiTurk Credentials are invalid.\n ',
            '  You cannot create ads and hits until you enter valid credentials in ',
            '  the \'psiTurk Access\' section of ~/.psiturkconfig.  You can obtain your',
            '  credentials or sign up at https://www.psiturk.org/login.\n'])
            
class InvalidAWSCredentialsError(AmtServicesWrapperError):
    def __init__(self, *args, **kwargs):
        super(InvalidAWSCredentialsError, self).__init__(*args, **kwargs)
        self.message = '\n'.join(['*****************************',
            '  Sorry, your AWS Credentials are invalid.\n ',
            '  You cannot create ads and hits until you enter valid credentials in ',
            '  the \'AWS Access\' section of ~/.psiturkconfig.  You can obtain your ',
            '  credentials via the Amazon AMT requester website.\n'])
            
class AdPsiturkOrgError(AmtServicesWrapperError):
    pass

class AdHtmlNotFoundError(AmtServicesWrapperError):
    def __init__(self, *args, **kwargs):
        super(AdHtmlNotFoundError, self).__init__(*args, **kwargs)
        self.message = '\n'.join(['*****************************',
            '  Sorry, there was an error registering ad.',
            '  The file ad.html is required to be in the templates folder',
            '  of your project so that the ad can be served.'])
            
class AdHtmlTooLarge(AmtServicesWrapperError):
    def __init__(self, size_of_ad, *args, **kwargs):
        super(AdHtmlTooLarge, self).__init__(*args, **kwargs)
        self.message = '\n'.join(['*****************************',
                                 '  Sorry, there was an error registering the ad.',
                                 '  Your local ad.html is {} bytes, but the maximum'.format(size_of_ad),
                                 '  template size uploadable to the ad server is',
                                 '  1048576 bytes.' ])