import {
    GET_VOUCHER,
    VOUCHER_ERROR,
    THROW_ERROR,
    LOADING,
} from '../actions/types';

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
                voucher: action.payload,
                loading: false,
            };
        case VOUCHER_ERROR:
            return {
                ...state,
                error: action.payload,
                voucher: null,
                loading: false,
            };
        case LOADING:
            return {
                ...state,
                loading: true,
            };
        case THROW_ERROR:
            return {
                ...state,
                error: null,
            };
        default:
            return state;
    }
};
