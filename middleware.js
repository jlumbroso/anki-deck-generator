module.exports = function (req, res, next) {
    if (/\.wasm$/.test(req.url)) {
        res.setHeader('Content-Type', 'application/wasm');
    }
    return next();
};
