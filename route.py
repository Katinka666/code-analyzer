import api
import logging

# logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_response(option, code):

    logging.info(f"Request for {option}")

    if option == "Hibakeresés":
        return api.analyze_error(code)
    if option == "Optimalizálás":
        return api.analyze_opt(code)
    if option == "Biztonsági elemzés":
        return api.analyze_sec(code)