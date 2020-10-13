import { combineReducers } from 'redux';
import voucherReducer from './voucherReducer';

export default combineReducers({
    voucher: voucherReducer,
});
