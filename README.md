# voucher-manager

A voucher checking app made w/ React &amp; Django.

# Installation

### Requirements

-   python >3.6 for Django
-   NodeJS/npm for ReactJS

### Steps

**Note**: Steps shown are done on a UNIX/POSIX machine. Steps may vary on a Windows machine.

#### Installing dependencies

```bash
  git clone $INSTALL_DIR
  cd $INSTALL_DIR
  (recommended) pipenv install instead
  pip3 install -r requirements.txt
  npm install
```

#### Local usage

In package.json, there are two scripts, dev & build. Use whichever suits you best by running

```
npm run dev/build
```

This builds the React frontend as well as sets up a watcher if you're using the dev option.

In the voucherapp directory, you can set up a Django server by running

```bash
python3 manage.py runserver
```

sqlite is currently used for the backend. If you wish to move it to a proper database like MySQL you will need to change settings.py and migrate again.

#### Admin panel credentials

The Django admin panel is located at localhost/site-admin/. Credentials are user: admin and password: password.

#### Test cases

Tests can be run by running

```bash
python3 manage.py test vouchers.tests.VoucherTestCase.{test_case_name}
```

Currently, there are only 2 test cases.

## Very IMPORTANT

-   Replace the secret key in settings.py and turn debug off if applicable.
-   There may be a flicker when entering the discount code on a local build. This is just a loading spinner and not an unintended bug.
-   If you're developing on top of this, npm might notice you of an intermediate vulnerability. However, the XSS vulnerability only affects `tooltip` and `autocomplete`
    components of materialize-css, which the app does not use. As of now, there are now security updates yet but do keep an eye on this as the developers are currently
    fixing this according to materialize-css' issue tracker.
