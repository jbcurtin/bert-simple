from bert import binding, utils, constants

@binding.follow('noop')
def first_aws_lambda_function():
    work_queue, done_queue, ologger = utils.comm_binders(first_aws_lambda_function)

    ologger.info('Awesome')
