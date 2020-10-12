import React, { Component } from 'react';

export class Header extends Component {
    render() {
        return (
            <nav>
                <div className='nav-wrapper blue darken-3 black-text'>
                    <a href='#' className='brand-logo center'>
                        <i className='material-icons'>book</i>
                    </a>
                </div>
            </nav>
        );
    }
}

export default Header;
