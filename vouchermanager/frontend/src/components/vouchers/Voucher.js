import React, { useEffect } from 'react';
import { getVoucher } from '../../actions/vouchers';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
import Preloader from '../layout/Preloader';

const Voucher = ({ voucher: { voucher, loading } }) => {
    // const { contacts, filtered, getContacts, loading } = contactContext;
    if (loading || voucher === null) {
        return <Preloader />;
    }

    return <h1>voucher found</h1>;
};

Voucher.propTypes = {
    voucher: PropTypes.object.isRequired,
    getVoucher: PropTypes.func.isRequired,
};

const mapStateToProps = (state) => ({
    voucher: state.voucher,
});

export default connect(mapStateToProps, { getVoucher })(Voucher);
