import requests

test_paths = {"buckets":[
"car-pics/Alfa Romeo_Stelvio_2020_43_18_280_20_4_74_66_184_22_AWD_5_4_SUV_jPE.jpg",
"car-pics/Alfa Romeo_Stelvio_2020_43_18_280_20_4_74_66_184_22_AWD_5_4_SUV_lno.jpg",
"car-pics/Alfa Romeo_Stelvio_2020_43_18_280_20_4_74_66_184_22_AWD_5_4_SUV_luF.jpg",
"car-pics/Alfa Romeo_Stelvio_2020_43_18_280_20_4_74_66_184_22_AWD_5_4_SUV_mHr.jpg",
"car-pics/Alfa Romeo_Stelvio_2020_43_18_280_20_4_74_66_184_22_AWD_5_4_SUV_meO.jpg",
"car-pics/Alfa Romeo_Stelvio_2020_43_18_280_20_4_74_66_184_22_AWD_5_4_SUV_mgV.jpg",
"car-pics/Alfa Romeo_Stelvio_2020_43_18_280_20_4_74_66_184_22_AWD_5_4_SUV_sXQ.jpg",
"car-pics/Alfa Romeo_Stelvio_2020_43_18_280_20_4_74_66_184_22_AWD_5_4_SUV_tCl.jpg",
"car-pics/Alfa Romeo_Stelvio_2020_43_18_280_20_4_74_66_184_22_AWD_5_4_SUV_uAU.jpg",
"car-pics/Alfa Romeo_Stelvio_2020_43_18_280_20_4_74_66_184_22_AWD_5_4_SUV_uDn.jpg",
"car-pics/Alfa Romeo_Stelvio_2020_43_18_280_20_4_74_66_184_22_AWD_5_4_SUV_uSa.jpg",
"car-pics/Alfa Romeo_Stelvio_2020_43_18_280_20_4_74_66_184_22_AWD_5_4_SUV_uWv.jpg",
"car-pics/Alfa Romeo_Stelvio_2020_43_18_280_20_4_74_66_184_22_AWD_5_4_SUV_wXj.jpg",
"car-pics/Alfa Romeo_Stelvio_2020_43_18_280_20_4_74_66_184_22_AWD_5_4_SUV_wit.jpg",
"car-pics/Alfa Romeo_Stelvio_2020_43_18_280_20_4_74_66_184_22_AWD_5_4_SUV_wlg.jpg",
"car-pics/Alfa Romeo_Stelvio_2020_43_18_280_20_4_74_66_184_22_AWD_5_4_SUV_xQt.jpg",
]}


HOST="http://localhost:8000"
#HOST = 'https://session-7nnso9xjmuoanecag439bm.anyscaleuserdata.com/serve'

def post_a_request():
    URL = f"{HOST}/start"
    response = requests.post(URL, json=test_paths)
    print(response.text)
    return response

def get_a_status():
    URL = f"{HOST}/status"
    response = requests.get(URL)
    print(response.text)
    return response


post_a_request()
get_a_status()

