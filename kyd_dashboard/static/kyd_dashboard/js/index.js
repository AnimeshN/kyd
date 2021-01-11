function parseURLParameters() {
  var query = (window.location.search || '?').substr(1);
  var map = [];
  query.replace(/([^&=]+)=?([^&]*)(?:&+|$)/g, function (match, key, value) {
    map.push(value);
  });
  return map;
}