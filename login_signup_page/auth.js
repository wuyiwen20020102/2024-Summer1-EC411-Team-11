const passport = require('passport');
const GoogleStrategy = require('passport-google-oauth2').Strategy;

const GOOGLE_CLIENT_ID = '412967482250-gb8bvpp05qq2d8seuhui8qjcl03ot54u.apps.googleusercontent.com';
const GOOGLE_CLIENT_SECRET = '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';

passport.use(new GoogleStrategy({
    clientID:     GOOGLE_CLIENT_ID,
    clientSecret: GOOGLE_CLIENT_SECRET,
    callbackURL: "http://localhost:5000/google/callback",
    passReqToCallback   : true
  },
  function(request, accessToken, refreshToken, profile, done) {
    /*User.findOrCreate({ googleId: profile.id }, function (err, user) {
      return done(err, user);
    });
    */
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