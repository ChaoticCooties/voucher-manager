import React, { useEffect, Fragment } from 'react';

import 'materialize-css/dist/css/materialize.min.css';
import M from 'materialize-css';

import Header from './layout/Header';
import VoucherSearch from './vouchers/VoucherSearch';
import Vouchers from './vouchers/Vouchers';

import { Provider } from 'react-redux';
import store from '../store';

const App = () => {
    useEffect(() => {
        // Init Materialize JS
        M.AutoInit();
    });

    return (
        <Provider store={store}>
            <Fragment>
                <Header />
                <div className='container'>
                    <VoucherSearch />
                    <Vouchers />
                </div>
            </Fragment>
        </Provider>
    );
};

export default App;
