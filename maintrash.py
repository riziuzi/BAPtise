import dill
import pyarrow.parquet as pq

# p = pq.read_table("./0.parquet")


# dill.dump_session("session.pkl")

dill.load_session('session.pkl')