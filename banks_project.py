import extract_data as ex
import transform_data as tf
import load_data as ld
import log_message as log

# ETL Start
log.log_process("ETL Started")

# Extract data
log.log_process('Extract started')
extracted_data = ex.extract_from_url()
# print(extracted_data)
log.log_process('Extract ended')

# Transform data
log.log_process('Transform started')
transformed_data = tf.transform_data(extracted_data)
print(transformed_data)
log.log_process('Transform ended')

# Load data
log.log_process('Load started')
ld.load_all(transformed_data)
log.log_process('Load end')

# ETL End
log.log_process('ETL Ended \n')
