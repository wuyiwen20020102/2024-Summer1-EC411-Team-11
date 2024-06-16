const passport = require('passport');
const GoogleStrategy = require('passport-google-oauth2').Strategy;

/*
const GOOGLE_CLIENT_ID = 'xxxxx';
const GOOGLE_CLIENT_SECRET = 'xxxxx'; //密钥放这里
*/

/*
passport.use(new GoogleStrategy({
    clientID:     GOOGLE_CLIENT_ID,
    clientSecret: GOOGLE_CLIENT_SECRET,
    callbackURL: "http://localhost:5000/google/callback",
    passReqToCallback   : true
  },
  function(request, accessToken, refreshToken, profile, done) {
    console.log('AccessToken:', accessToken);
    console.log('Profile:', profile);
    return done(null, profile);
  }
));

passport.serializeUser(function(user,done) {
    done(null, user);
});

passport.deserializeUser(function(user,done) {
    done(null, user);
});
*/