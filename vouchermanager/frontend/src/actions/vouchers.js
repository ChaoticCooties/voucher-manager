import { GET_VOUCHER, VOUCHER_ERROR, SET_LOADING } from './types';

// Fetch voucher from given code with api call
export const getVoucher = (code) => async (dispatch) => {
    try {
        // Toggle loader
        setLoading();

        // Fetch from api and return json
        const res = await fetch(`/api/vouchers/${code}`);
        const data = await res.json();

        dispatch({
            type: GET_VOUCHER,
            payload: data,
        });
    } catch (err) {
        dispatch({
            type: VOUCHER_ERROR,
            payload: err.response.statusText,
        });
    }
};

// Set loading to true
export const setLoading = () => {
    return {
        type: SET_LOADING,
    };
};
