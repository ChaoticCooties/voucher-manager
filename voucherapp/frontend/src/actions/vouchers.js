import axios from 'axios';
import { GET_VOUCHER, VOUCHER_ERROR, LOADING } from './types';

// Fetch voucher from given code with api call
export const getVoucher = (code) => (dispatch) => {
    dispatch({
        type: LOADING,
    });

    // HTTP fetch from api
    axios
        .get(`api/vouchers/${code}`)
        .then((res) => {
            dispatch({
                type: GET_VOUCHER,
                payload: res.data,
            });
        })
        .catch((err) => {
            dispatch({
                type: VOUCHER_ERROR,
                payload: err.response.data,
            });
        });
};
