import superagent from 'superagent';
import camelize from 'camelize';

function urlFor(resource) {
  return '/api' + resource;
}

export default function request({ method = 'get', url, body, headers = {} }) {
  const req = superagent[method].call(request, urlFor(url));

  for (const header in headers) {
    req.set(header, headers[header]);
  }

  if (body) {
    req.send(body);
  }

  return new Promise((resolve, reject) => {
    req.end((err, res) => {
      if (err) return reject(err);
      if (!res.ok) return reject(new Error(res.body));
      return resolve(camelize(res.body));
    });
  });
}

export function callAPI(action) {
  return (dispatch, getState) => {
    const { method, endpoint, body } = action;
    const options = {
      method,
      url: endpoint,
      body
    };

    return dispatch({
      type: action.type,
      promise: request(options)
    });
  };
}
