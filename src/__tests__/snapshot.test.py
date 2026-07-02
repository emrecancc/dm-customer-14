import { render } from '@testing-library/react';
import { Dashboard } from '../Dashboard';

test('Dashboard renders correctly', () => {
  const { asFragment } = render(<Dashboard />);
  expect(asFragment()).toMatchSnapshot(); // fails when date changes
});
