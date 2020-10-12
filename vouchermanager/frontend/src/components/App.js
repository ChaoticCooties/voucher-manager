import React, { useEffect, Fragment } from 'react';

import Header from './layout/Header';
import Vouchers from './vouchers/VoucherSearch';

import { Provider } from 'react-redux';
import store from '../store';

import 'materialize-css/dist/css/materialize.min.css';
import M from 'materialize-css';

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
                    <Vouchers />
                </div>
            </Fragment>
        </Provider>
    );
};

export default App;
