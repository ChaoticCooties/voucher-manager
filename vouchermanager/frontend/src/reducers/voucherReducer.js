import { GET_VOUCHER, VOUCHER_ERROR, SET_LOADING } from '../actions/types';

const initialState = {
    voucher: null,
    loading: false,
    error: null,
};

export default (state = initialState, action) => {
    switch (action.type) {
        case GET_VOUCHER:
            return {
                ...state,
                vouchers: action.payload,
                loading: false,
            };
        case VOUCHER_ERROR:
            return {
                ...state,
                error: action.payload,
            };
        case SET_LOADING:
            return {
                ...state,
                loading: true,
            };
        default:
            return state;
    }
};
