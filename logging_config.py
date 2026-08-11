import logging,sys
def setup(level=logging.INFO):
 logging.basicConfig(level=level,format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",handlers=[logging.StreamHandler(sys.stdout)])
